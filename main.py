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
    if args.utf8:
        print(printer.utf8())
        return
    if args.utf16:
        print(printer.utf16())
        return
    if args.utf32:
        print(printer.utf32())
        return
    print('UTF-8:', printer.utf8())
    print('UTF-16:', printer.utf16())
    print('UTF-32:', printer.utf32())


if __name__ == '__main__':
    main()
