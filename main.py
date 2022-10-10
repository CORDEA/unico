import argparse


def utf8(text):
    return ' '.join([hex(r) for r in bytes(text, 'utf-8')])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--utf32', action='store_true')
    parser.add_argument('--utf16', action='store_true')
    parser.add_argument('--utf8', action='store_true')
    parser.add_argument('text')
    args = parser.parse_args()
    print(utf8(args.text))


if __name__ == '__main__':
    main()
