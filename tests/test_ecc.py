from itertools import product

from ecc import decode, decode_with_status, encode, inject_single_bit_error


def test_all_single_bit_errors_are_corrected_for_all_messages():
    """Every Hamming (7,4) codeword should recover from one flipped bit."""
    for message in map("".join, product("01", repeat=4)):
        encoded = encode(message)

        for error_index in range(7):
            corrupted = encoded.copy()
            corrupted[error_index] ^= 1

            recovered, corrected_position = decode_with_status(corrupted)
            assert recovered == list(map(int, message))
            assert corrected_position == error_index + 1
            assert decode(corrupted) == list(map(int, message))


def test_error_injection_is_reproducible_and_does_not_mutate_codeword():
    encoded = encode("0101")
    corrupted = inject_single_bit_error(encoded, 4)

    assert encoded == [0, 1, 0, 0, 1, 0, 1]
    assert corrupted == [0, 1, 0, 1, 1, 0, 1]


def test_error_injection_rejects_invalid_position():
    try:
        inject_single_bit_error(encode("0101"), 8)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for an out-of-range error position")


def test_encode_rejects_invalid_message_lengths_and_values():
    for invalid in ("", "101", "10101", "10a1"):
        try:
            encode(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError(f"Expected ValueError for {invalid!r}")
