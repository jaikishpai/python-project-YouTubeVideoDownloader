import argparse


parser = argparse.ArgumentParser(description='Process a string.')
parser.add_argument('s', type=str, help='string for construct class')
args = parser.parse_args()


class Creator:

    def __init__(self, s):
        self.s = s
        self.name_list = None

    def check_legal(self):
        return True

    def output(self):
        if not self.check_legal():
            return False

        self.names = self.s.split('(')
        f = open("src.py", "w")
        body = f"class {self.names[-1]}:\n"\
               "\n"\
               "    def __init__(self):\n"\
               "        pass\n"\
               "\n\n"
        f.write(body)
        for c, p in zip(self.names[-2::-1], self.names[:0:-1]):
            body = f"class {c}({p}):\n" +\
                    "\n" +\
                    "    def __init__(self):\n" +\
                    "        pass\n" +\
                    "\n\n"
            f.write(body)


def main():
    c = Creator(args.s)
    c.output()


if __name__ == '__main__':
    main()
