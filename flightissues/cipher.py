import re
from flightissues.constants import ROWS, SEATS


class InvalidCipherException(BaseException):
    """
    Exception used by the Cipher class when an invalid cipher is used to
    construct an instance.
    """

    pass


class Cipher:
    """
    Cipher class, responsible for transforming the boarding pass identifier into
    a more readable format.
    """

    def __init__(self, value: str) -> None:
        """
        Initializes the Cipher instance. Raises an exception if the cipher does
        not respect the following format: '^[FB]{7}[LR]{3}$'
        """

        pattern = re.compile("^[FB]{7}[LR]{3}$")

        if pattern.match(value) is None:
            raise InvalidCipherException

        self.__value = value

    def split_low(self, lower: int, upper: int) -> tuple[int, int]:
        """
        Splits the bounds in the middle and conserves the lower part
        """

        return lower, (lower + upper) // 2

    def split_high(self, lower: int, upper: int) -> tuple[int, int]:
        """
        Splits the bounds in the middle and conserves the upper part
        """

        return (lower + upper) // 2, upper

    def decipher(self) -> tuple[int, int, int]:
        """
        Returns the row, seat and id for a designated cipher
        """

        splitters = {
            "F": self.split_low,
            "L": self.split_low,
            "B": self.split_high,
            "R": self.split_high,
        }

        row, seat = 0, 0
        rowCipher, seatCipher = self.__value[:7], self.__value[7:]

        # Determine the row the cipher points to
        lower, upper = 0, ROWS
        for symbol in rowCipher:
            lower, upper = splitters[symbol](lower, upper)

        row = lower

        # Determine the seat the cipher points to
        lower, upper = 0, SEATS
        for symbol in seatCipher:
            lower, upper = splitters[symbol](lower, upper)

        seat = lower

        return row, seat, row * SEATS + seat
