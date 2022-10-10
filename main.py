import argparse
from enum import Enum
from textwrap import wrap


class Format(Enum):
    HEX = 'hex'
    BINARY = 'binary'

    def __str__(self):
        return self.value


class Printer:
    def __init__(self, text, sep, fmt):
        self.text = text
        self.sep = sep
        self.fmt = fmt

    def utf8(self):
        return self.sep.join([self.format(r, 8) for r in bytes(self.text, 'utf-8')])

    def utf16(self):
        b = iter(bytes(self.text.encode('utf-16-be')))
        return self.sep.join([self.format(c[0] << 8 | c[1], 16) for c in zip(b, b)])

    def utf32(self):
        return self.sep.join([self.format(ord(c), 32) for c in self.text])

    def format(self, query, digit):
        if self.fmt == Format.HEX:
            return hex(query)
        return ' '.join(wrap(bin(query)[2:].zfill(digit), 4))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--utf32', action='store_true')
    parser.add_argument('--utf16', action='store_true')
    parser.add_argument('--utf8', action='store_true')
    parser.add_argument('--sep', default=' ')
    parser.add_argument('--format', type=Format, choices=Format, default=Format.HEX)
    parser.add_argument('text')
    args = parser.parse_args()
    printer = Printer(args.text, args.sep, args.format)
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
