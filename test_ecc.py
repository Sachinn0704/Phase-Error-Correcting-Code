import unittest

from ecc import decode, encode


class TestHammingECC(unittest.TestCase):
    def test_round_trip(self):
        self.assertEqual(decode(encode("1011")), [1, 0, 1, 1])

    def test_corrects_each_single_bit_error(self):
        original = "1011"
        encoded = encode(original)

        for index in range(7):
            corrupted = encoded.copy()
            corrupted[index] ^= 1
            self.assertEqual(
                decode(corrupted),
                [1, 0, 1, 1],
                msg=f"Failed to correct bit at position {index + 1}",
            )

    def test_rejects_invalid_input(self):
        with self.assertRaises(ValueError):
            encode("101")
        with self.assertRaises(ValueError):
            encode("10x1")
        with self.assertRaises(ValueError):
            decode([0, 1, 0])


if __name__ == "__main__":
    unittest.main()
