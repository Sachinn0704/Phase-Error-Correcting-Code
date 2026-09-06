def encode(bits):
    """Encode exactly four data bits using a Hamming (7,4) code."""
    if len(bits) != 4 or any(bit not in "01" for bit in bits):
        raise ValueError("Hamming (7,4) encoding requires exactly four binary bits")

    d = list(map(int, bits))
    p1 = d[0] ^ d[1] ^ d[3]
    p2 = d[0] ^ d[2] ^ d[3]
    p3 = d[1] ^ d[2] ^ d[3]
    return [p1, p2, d[0], p3, d[1], d[2], d[3]]


def decode(code):
    """Correct one-bit errors and return the four recovered data bits."""
    if len(code) != 7 or any(bit not in (0, 1) for bit in code):
        raise ValueError("Hamming (7,4) decoding requires exactly seven binary bits")

    code = list(code)
    p1, p2, d0, p3, d1, d2, d3 = code
    s1 = p1 ^ d0 ^ d1 ^ d3
    s2 = p2 ^ d0 ^ d2 ^ d3
    s3 = p3 ^ d1 ^ d2 ^ d3
    pos = s1 * 1 + s2 * 2 + s3 * 4

    if pos != 0:
        code[pos - 1] ^= 1

    return [code[2], code[4], code[5], code[6]]
