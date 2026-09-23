def encode(bits):
    """Encode exactly four data bits using a Hamming (7,4) code."""
    if len(bits) != 4 or any(bit not in "01" for bit in bits):
        raise ValueError("Hamming (7,4) encoding requires exactly four binary bits")

    d = list(map(int, bits))
    p1 = d[0] ^ d[1] ^ d[3]
    p2 = d[0] ^ d[2] ^ d[3]
    p3 = d[1] ^ d[2] ^ d[3]
    return [p1, p2, d[0], p3, d[1], d[2], d[3]]


def inject_single_bit_error(code, position):
    """Return a copy of a Hamming codeword with one selected bit flipped.

    ``position`` is one-based (1 through 7), matching the syndrome position
    reported by :func:`decode_with_status`.
    """
    if len(code) != 7 or any(bit not in (0, 1) for bit in code):
        raise ValueError("Hamming (7,4) error injection requires seven binary bits")
    if not 1 <= position <= 7:
        raise ValueError("Error position must be between 1 and 7")

    corrupted = list(code)
    corrupted[position - 1] ^= 1
    return corrupted


def decode_with_status(code):
    """Correct one-bit errors and return recovered bits plus correction metadata."""
    if len(code) != 7 or any(bit not in (0, 1) for bit in code):
        raise ValueError("Hamming (7,4) decoding requires exactly seven binary bits")

    code = list(code)
    p1, p2, d0, p3, d1, d2, d3 = code
    s1 = p1 ^ d0 ^ d1 ^ d3
    s2 = p2 ^ d0 ^ d2 ^ d3
    s3 = p3 ^ d1 ^ d2 ^ d3
    correction_position = s1 * 1 + s2 * 2 + s3 * 4

    if correction_position != 0:
        code[correction_position - 1] ^= 1

    recovered = [code[2], code[4], code[5], code[6]]
    return recovered, correction_position


def decode(code):
    """Correct one-bit errors and return the four recovered data bits."""
    recovered, _ = decode_with_status(code)
    return recovered
