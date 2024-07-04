from argparse import ArgumentParser, Namespace
from typing import List


def parse_arguments() -> Namespace:
    """
    Fetch arguments from the command line
    """
    commandlineParser = ArgumentParser()

    commandlineParser.add_argument("path", help="The input file for the algorithm")
    commandlineParser.add_argument("-c", "--chart", action="store_true", required=False)

    arguments = commandlineParser.parse_args()

    return arguments


def parse_input_file(path: str) -> List[str]:
    """
    Read input file, and transform the data so that it can be processed
    """
    file = None

    try:
        file = open(path, "r")
    except OSError as error:
        print(error)
        exit(1)

    return file.read().splitlines()
