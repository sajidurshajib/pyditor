import sys
from dist import Reader, Printer


def main():
    # print(sys.argv[1])
    reader = Reader(sys.argv[1])
    txt = reader.read_only()
    printer = Printer(text_body=txt)
    printer.print_only(strip=True)


if __name__ == "__main__":
    main()
