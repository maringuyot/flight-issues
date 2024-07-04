from typing import List
from flightissues.cipher import Cipher
from flightissues.constants import ROWS, SEATS


def __find_seat(seating_chart) -> int:
    """
    Find our lost seat using the seating chart of the plane.
    """
    found_first_seat = False

    for i in range(len(seating_chart)):
        seat = seating_chart[i]

        # We found our seat!
        if found_first_seat and seat is None:
            return seating_chart[i - 1] + 1

        if seat is not None:
            found_first_seat = True

    return None


def compute(lines: List[str]) -> int:
    """
    Main algorithm. Returns our seat ID.
    """

    # Create a seating chart that we will fill in progressively
    seating_chart = [None for _ in range(ROWS * SEATS)]

    # Fill the seating chart using a set of known seats
    for line in lines:
        row, seat, id = Cipher(line).decipher()

        seating_chart[row * SEATS + seat] = id

    # Let's find our seat!
    return __find_seat(seating_chart)
