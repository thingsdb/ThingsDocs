#!/usr/bin/env python
"""
should_pass:
    the code should return with a valid response
should_err:
    the code should return with an exception
syntax_only:
    the code will be only checked for syntax
json_response:
    the return value should be equal to the JSON below the thingsdb code
no_test:
    not tested
"""
import sys
import os
import re
import json
from lib import run_test
from lib import default_test_setup
from lib.testbase import TestBase
from lib.client import get_client
from thingsdb.exceptions import ThingsDBError
from thingsdb.exceptions import AssertionError
from thingsdb.exceptions import ValueError


ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DOC_VERSION = os.getenv('DOC_VERSION')
if not DOC_VERSION:
    sys.exit(
        'expecting an environment variable DOC_VERSION\n'
        'for eaxmple: DOC_VERSION=v1')

CONTENT_PATH = os.path.join(ROOT_PATH, DOC_VERSION, 'content')
RE_TEST = re.compile(
    r'```thingsdb,([a-zA-Z_]*)(,(@[\:a-zA-Z0-9]))?')

RE_LINK = re.compile(r'(\[[\w\s\-\(\)\.]+\]\(([\.\/\w\-]+)\))')


class TestDoc(TestBase):

    title = 'Test documentation'

    @default_test_setup(num_nodes=1, seed=1, threshold_full_storage=1000)
    async def run(self):

        await self.node0.init_and_run()

        client = await get_client(self.node0)
        client.set_default_scope('//stuff')

        for root, dirs, files in os.walk(CONTENT_PATH):
            for file in files:
                if file.endswith(".md"):
                    fn = os.path.join(root, file)
                    with open(fn, 'r') as f:
                        lines = f.readlines()

                    location = root if file == '_index.md' else \
                        os.path.join(root, os.path.splitext(file)[0])

                    try:
                        await self.process_markdown(client, location, lines)
                    except Exception as e:
                        try:
                            ex = type(e)(
                                f'{e} happens in `{fn}`').with_traceback(
                                    sys.exc_info()[2])
                            raise ex
                        except Exception:
                            raise Exception(
                                f'{e} happens in `{fn}`').with_traceback(
                                    sys.exc_info()[2])

        client.close()
        await client.wait_closed()

    async def process_markdown(self, client, location, lines):
        lines = iter(lines)

        while True:
            try:
                line = next(lines)
                matches = RE_LINK.findall(line)
                for m in matches:
                    chap_fn = os.path.join(location, m[1], '_index.md')
                    mark_fn = os.path.join(location, f'{m[1]}.md')
                    chap_fn = os.path.abspath(chap_fn)
                    mark_fn = os.path.abspath(mark_fn)

                    if (not os.path.isfile(chap_fn)) and \
                            (not os.path.isfile(mark_fn)):
                        raise FileNotFoundError(
                            f'neither `{mark_fn}` or `{chap_fn}` exists')

                m = RE_TEST.match(line)
                if m:
                    scope = m.group(3)
                    await client.query(r'''
                        try(del_collection('stuff'));
                        try(del_user('iris'));
                        new_collection('stuff');
                    ''', scope='@t')
                    await self.MAP[m.group(1)](self, client, scope, lines)
            except StopIteration:
                break

    @staticmethod
    def get_code(lines):
        code = []
        while True:
            line = next(lines)
            if line.startswith('```'):
                break
            code.append(line)
        return ''.join(code)

    async def should_pass(self, client, scope, lines):
        code = self.get_code(lines)
        await client.query(code, scope=scope)

    async def should_err(self, client, scope, lines):
        code = self.get_code(lines)
        with self.assertRaises(ThingsDBError):
            await client.query(code, scope=scope)

    async def syntax_only(self, client, scope, lines):
        code = self.get_code(lines)
        code = f'assert(0); {code}'
        with self.assertRaises(AssertionError):
            await client.query(code, scope=scope)

    async def json_response(self, client, scope, lines):
        code = self.get_code(lines)
        res = await client.query(code, scope=scope)

        while True:
            try:
                line = next(lines)
                if line.startswith('```json'):
                    expected = json.loads(self.get_code(lines))
                    break
            except StopIteration:
                raise ValueError('missing JSON response not found')

        self.assertEqual(res, expected)

    async def no_test(self, client, scope, lines):
        code = self.get_code(lines)
        pass

    MAP = {
        'should_pass': should_pass,
        'should_err': should_err,
        'syntax_only': syntax_only,
        'json_response': json_response,
        'no_test': no_test,

    }


if __name__ == '__main__':
    run_test(TestDoc())
