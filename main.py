import argparse


def utf8(text):
    return ' '.join([hex(r) for r in bytes(text, 'utf-8')])


def utf16(text):
    b = iter(bytes(text.encode('utf-16-be')))
    return ' '.join([hex(c[0] << 8 | c[1]) for c in zip(b, b)])


def utf32(text):
    return ' '.join([hex(ord(c)) for c in text])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--utf32', action='store_true')
    parser.add_argument('--utf16', action='store_true')
    parser.add_argument('--utf8', action='store_true')
    parser.add_argument('text')
    args = parser.parse_args()
    print(utf16(args.text))


if __name__ == '__main__':
    main()
