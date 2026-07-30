from argparse import Namespace
from io import TextIOWrapper
from logging import getLogger

logger = getLogger(__name__)


def do_example(args: Namespace) -> None:
    logger.info("-> argparse example started: %s", args)

    inputs: list[TextIOWrapper] = args.infiles
    output: TextIOWrapper = args.outfile

    try:
        for input in inputs:
            for line in input:
                # line contains newline
                output.write(line)

            # argparse.FileType does not close.
            if input.name != "<stdin>":
                input.close()

    except KeyboardInterrupt:
        logger.warning("interrupt!")

    # argparse.FileType does not close.
    if output.name != "<stdout>":
        output.close()
