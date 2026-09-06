import random

from enc import manchester, show
from ecc import decode, encode


def run():
    bits = input("Enter exactly four binary bits: ").strip()
    if len(bits) != 4 or any(bit not in "01" for bit in bits):
        raise ValueError("Please enter exactly four binary bits, for example 1011")

    print("Input:", bits)

    encoded = encode(bits)
    print("Hamming Encoded:", encoded)

    error_position = random.randint(0, len(encoded) - 1)
    encoded[error_position] ^= 1
    print("With Error:", encoded)
    print("Injected Error Position:", error_position + 1)

    corrected = decode(encoded)
    print("Corrected Output:", corrected)

    signal = manchester(bits)
    show(signal)
    print("Graph saved as graph.png")


if __name__ == "__main__":
    run()
