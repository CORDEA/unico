import argparse


class Printer:
    def __init__(self, text, sep):
        self.text = text
        self.sep = sep

    def utf8(self):
        return self.sep.join([hex(r) for r in bytes(self.text, 'utf-8')])

    def utf16(self):
        b = iter(bytes(self.text.encode('utf-16-be')))
        return self.sep.join([hex(c[0] << 8 | c[1]) for c in zip(b, b)])

    def utf32(self):
        return self.sep.join([hex(ord(c)) for c in self.text])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--utf32', action='store_true')
    parser.add_argument('--utf16', action='store_true')
    parser.add_argument('--utf8', action='store_true')
    parser.add_argument('--sep', default=' ')
    parser.add_argument('text')
    args = parser.parse_args()
    printer = Printer(args.text, args.sep)
    print(printer.utf16())


if __name__ == '__main__':
    main()
