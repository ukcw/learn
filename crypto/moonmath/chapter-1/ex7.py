import unittest

"""
Exercise 7 (Binary Representation). Write an algorithm that computes the binary representation of any non-negative integer.
"""


def binary_representation(n):
    if n == 0:
        return "0"

    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    return binary_representation(n // 2) + str(n % 2) if n > 1 else str(n % 2)


class TestDecimalToBinary(unittest.TestCase):
    def test_normal_cases(self):
        self.assertEqual(binary_representation(13), "1101")
        self.assertEqual(binary_representation(42), "101010")
        self.assertEqual(binary_representation(255), "11111111")

    def test_edge_cases(self):
        self.assertEqual(binary_representation(0), "0")
        self.assertEqual(binary_representation(1), "1")
        self.assertEqual(binary_representation(1023), "1111111111")

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            binary_representation(-1)


if __name__ == "__main__":
    unittest.main()
