import flightissues.inputparser as inputparser
import flightissues.algorithm as algorithm

if __name__ == "__main__":
    # Parse command line arguments, and normalize input data
    arguments = inputparser.parse_arguments()
    ciphers = inputparser.parse_input_file(arguments.path)

    # Compute our seat id
    seat_id, seating_chart = algorithm.compute(ciphers)

    if arguments.chart:
        print(seating_chart)
        print("==============================")

    print(f"Seat ID: {seat_id}")
