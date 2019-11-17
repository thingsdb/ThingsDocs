import re
import os


WEIGHT = re.compile(r'^weight\s*:\s*([0-9]+)\r?\n')


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
CONTENT_PATH = os.path.join(ROOT_PATH, 'content')


class Page:
    def __init__(self, name):
        pass


class Secton:
    def __init__(self, parent):
        self.parent = parent



def get_weight_map():
    # section = Section(None)


    for root, dirs, files in os.walk(CONTENT_PATH):
        for file in files:
            if file.endswith(".md"):
                if file == '_index.md':
                    pass

                fn = os.path.join(root, file)
                with open(fn, 'r') as f:
                    lines = f.readlines()

                for line in lines:
                    m = WEIGHT.match(line)
                    if m:
                        print(m.group(1))

        print(root)
        # section = section.parent

if __name__ == '__main__':
    get_weight_map()
