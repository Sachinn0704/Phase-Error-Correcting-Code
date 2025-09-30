import random
from enc import manchester, show
from ecc import encode, decode

def run():
    bits_length = int(input("Enter the length of the bit string: "))
    bits = ''.join(random.choice('01') for _ in range(bits_length))
    print("Input:", bits)

    encoded = encode(bits)
    print("Hamming Encoded:", encoded)

    error_position = random.randint(0, len(encoded) - 1)
    encoded[error_position] ^= 1
    print("With Error:", encoded)

    corrected = decode(encoded)
    print("Corrected Output:", corrected)

    signal = manchester(bits)
    show(signal)
    print("Graph saved as graph.png")

run()


