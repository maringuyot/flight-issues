import json
import unittest
from flightissues.cipher import Cipher, InvalidCipherException


class TestCipherMethods(unittest.TestCase):
    def setUp(self):
        """
        Load json test data
        """

        ciphers_invalid_json_file = open("tests/resources/ciphers_invalid.json")
        ciphers_json_file = open("tests/resources/ciphers.json")
        splits_json_file = open("tests/resources/splits.json")

        self.cipher_invalid_resources = json.load(ciphers_invalid_json_file)
        self.cipher_resources = json.load(ciphers_json_file)
        self.splits_resources = json.load(splits_json_file)

        ciphers_invalid_json_file.close()
        ciphers_json_file.close()
        splits_json_file.close()

    def test_invalid_cipher(self):
        """
        Test Cipher's ability to detect an invalid cipher
        """

        for index, cipher_invalid_resource in enumerate(self.cipher_invalid_resources):
            with self.subTest(f"Invalid cipher {index + 1}"):

                def execute():
                    cipher = Cipher(cipher_invalid_resource)

                self.assertRaises(InvalidCipherException, execute)

    def test_decipher(self):
        """
        Test Cipher's 'decipher' function
        """

        for index, cipher_resource in enumerate(self.cipher_resources):
            with self.subTest(f"Decipher {index + 1}"):
                cipher = Cipher(cipher_resource["cipher"])
                row, seat, id = cipher.decipher()

                self.assertEqual(row, cipher_resource["result"]["row"])
                self.assertEqual(seat, cipher_resource["result"]["seat"])
                self.assertEqual(id, cipher_resource["result"]["id"])

    def test_split_low(self):
        """
        Test Cipher's 'split_low' function
        """

        for index, split_resource in enumerate(self.splits_resources):
            with self.subTest(f"Split low {index + 1}"):
                cipher = Cipher("BFFFBBFRRR")

                lower, upper = cipher.split_low(
                    split_resource["lower"], split_resource["upper"]
                )

                self.assertEqual(lower, split_resource["results"]["low"]["lower"])
                self.assertEqual(upper, split_resource["results"]["low"]["upper"])

    def test_split_high(self):
        """
        Test Cipher's 'split_high' function
        """

        for index, split_resource in enumerate(self.splits_resources):
            with self.subTest(f"Split high {index + 1}"):
                cipher = Cipher("BFFFBBFRRR")

                lower, upper = cipher.split_high(
                    split_resource["lower"], split_resource["upper"]
                )

                self.assertEqual(lower, split_resource["results"]["high"]["lower"])
                self.assertEqual(upper, split_resource["results"]["high"]["upper"])


if __name__ == "__main__":
    print("Hello World!")
    unittest.main()
