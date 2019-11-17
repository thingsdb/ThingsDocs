#!/usr/bin/env python
import sys
import re
import os
import operator
import argparse


WEIGHT = re.compile(r'^weight\s*:\s*([0-9]+)\r?\n')

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
CONTENT_PATH = os.path.join(ROOT_PATH, 'content')


class Page:
    def __init__(self, name):
        self.name = name
        self.weight = 0

    def set_weight(self, weight):
        self.weight = weight


class Section(Page):
    def __init__(self, name, parent):
        super().__init__(name)
        self.parent = parent
        self.pages = []

    def ensure_section(self, name):
        for page in self.pages:
            if page.name == name:
                assert isinstance(page, Section)
                return page
        section = Section(name, self)
        self.pages.append(section)
        return section

    def add_page(self, name):
        page = Page(name)
        self.pages.append(page)
        return page

    def echo(self, indent):
        self.pages.sort(key=operator.attrgetter('weight'))
        for page in self.pages:
            print(f'{"    " * indent}{page.name}')
            if isinstance(page, Section):
                page.echo(indent+1)


def get_weight_map():
    site = Section('', None)

    weight = 1
    for root, dirs, files in os.walk(CONTENT_PATH):
        uri = root[len(CONTENT_PATH):]
        uri = uri.strip('/').split('/')
        section = site
        for s in uri:
            if s:
                section = section.ensure_section(s)

        files.sort()
        for file in files:
            if file.endswith(".md"):
                if file == '_index.md':
                    page = section
                else:
                    page = section.add_page(os.path.splitext(file)[0])

                fn = os.path.join(root, file)
                with open(fn, 'r') as f:
                    lines = f.readlines()

                for i, line in enumerate(lines):
                    m = WEIGHT.match(line)
                    if m:
                        page.set_weight(int(m.group(1)))
                        break

    site.echo(0)


def set_weights(fn):
    with open(fn, 'r') as f:
        lines = f.readlines()

    indent = [0]
    uri = ['']
    ident = 0
    weight = 1
    for line in lines:
        leading_spaces = len(line) - len(line.strip(' '))
        if leading_spaces > indent[-1]:
            indent.append(leading_spaces)
        else:
            while True:
                if leading_spaces == indent[-1]:
                    break
                indent.pop()
        uri = uri[:len(indent)]
        uri.append(line.strip())
        fn = os.path.join(CONTENT_PATH, *uri)
        chap_fn = os.path.join(fn, '_index.md')
        page_fn = fn + '.md'
        if os.path.isfile(chap_fn):
            fn = chap_fn
        elif os.path.isfile(page_fn):
            fn = page_fn
        else:
            raise FileNotFoundError(
                f'neither `{chap_fn}` or `{page_fn}` is found')

        with open(fn, 'r') as f:
            doc_lines = f.readlines()

        for i, doc_line in enumerate(doc_lines):
            m = WEIGHT.match(doc_line)
            if m:
                doc_lines[i] = f'weight: {weight}\n'
                weight += 1
                break

        with open(fn, 'w') as f:
            f.writelines(doc_lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--export',
        action='store_true',
        help='export current site structure by weights')
    parser.add_argument(
        '--apply',
        help='set weights according a site structure file')

    args = parser.parse_args()

    if not args.export and not args.apply:
        parser.print_help()
        sys.exit(0)

    if args.export:
        get_weight_map()

    if args.apply:
        set_weights(args.apply)
