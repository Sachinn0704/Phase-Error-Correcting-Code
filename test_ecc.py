import unittest

from ecc import decode, decode_with_status, encode


class TestHammingECC(unittest.TestCase):
    def test_round_trip_for_all_four_bit_messages(self):
        for value in range(16):
            original = format(value, "04b")
            with self.subTest(original=original):
                self.assertEqual(decode(encode(original)), list(map(int, original)))

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

    def test_decode_status_reports_corrected_position(self):
        encoded = encode("1011")

        for index in range(7):
            corrupted = encoded.copy()
            corrupted[index] ^= 1
            recovered, correction_position = decode_with_status(corrupted)
            self.assertEqual(recovered, [1, 0, 1, 1])
            self.assertEqual(correction_position, index + 1)

    def test_decode_status_reports_zero_for_clean_code(self):
        recovered, correction_position = decode_with_status(encode("1011"))
        self.assertEqual(recovered, [1, 0, 1, 1])
        self.assertEqual(correction_position, 0)

    def test_rejects_invalid_input(self):
        with self.assertRaises(ValueError):
            encode("101")
        with self.assertRaises(ValueError):
            encode("10x1")
        with self.assertRaises(ValueError):
            decode([0, 1, 0])


if __name__ == "__main__":
    unittest.main()
