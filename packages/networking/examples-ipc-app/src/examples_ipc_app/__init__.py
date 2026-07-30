from .arguments import parse_arguments


def main() -> int:
    args = parse_arguments()

    try:
        args.exec(args)

    except Exception as e:
        print(type(e), e)

    return 0
