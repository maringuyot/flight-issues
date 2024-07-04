import flightissues.inputparser as inputparser
import flightissues.algorithm as algorithm

if __name__ == "__main__":
    # Parse command line arguments, and normalize input data
    arguments = inputparser.parse_arguments()
    ciphers = inputparser.parse_input_file(arguments.path)

    # Compute our seat id
    seat_id = algorithm.compute(ciphers)

    print(f"Seat ID: {seat_id}")
