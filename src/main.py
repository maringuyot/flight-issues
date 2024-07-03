import argparse

# Initialize the command line parser, and fetch the arguments
commandlineParser = argparse.ArgumentParser()
commandlineParser.add_argument("path", help="The input file for the algorithm")

arguments = commandlineParser.parse_args()

# Open the file and clean up the data

path = arguments.path
file = None

try:
    file = open(path, "r")
except OSError as error:
    print(error)
    exit(1)

lines = file.read().splitlines()
print(lines)
