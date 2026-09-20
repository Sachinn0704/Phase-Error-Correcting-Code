from itertools import product

from ecc import decode, encode


def test_all_single_bit_errors_are_corrected_for_all_messages():
    """Every Hamming (7,4) codeword should recover from one flipped bit."""
    for message in map("".join, product("01", repeat=4)):
        encoded = encode(message)

        for error_index in range(7):
            corrupted = encoded.copy()
            corrupted[error_index] ^= 1

            assert decode(corrupted) == list(map(int, message))


def test_encode_rejects_invalid_message_lengths_and_values():
    for invalid in ("", "101", "10101", "10a1"):
        try:
            encode(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError(f"Expected ValueError for {invalid!r}")
