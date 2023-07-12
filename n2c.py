from argparse import ArgumentParser
from names import get_full_name
from subprocess import Popen, PIPE


def generate_name(gender: str = "female") -> str:
    return get_full_name(gender=gender)


def copy_string_to_clipboard(data: str):
    Popen(('clip'), stdin=PIPE).communicate(data.encode())


def main():
    parser = ArgumentParser(
        description='use names module to generate names and push them to clipboard')
    parser.add_argument('-m', '--male',
                        help="male frist name, if not set it will be female",
                        action='store_true',
                        default=False)
    parser.add_argument('-s', '--show',
                        help="print name to console",
                        action='store_true',
                        default=False)
    args = parser.parse_args()
    if args.male is not None:
        if args.male:
            name = generate_name(gender="male")
        else:
            name = generate_name(gender="female")
        copy_string_to_clipboard(name)
        if args.show is True:
            print(name)
    else:
        print(args)


if __name__ == "__main__":
    main()
