import numpy as np
import matplotlib.pyplot as plt

def manchester(bits):
    signal = []
    for b in bits:
        if b == '0':
            signal += [1, -1]
        else:
            signal += [-1, 1]
    return signal

def show(signal):
    t = range(len(signal))
    plt.step(t, signal, where='post')
    plt.ylim(-2, 2)
    plt.title("Manchester Encoding")
    plt.grid(True)
    plt.savefig("graph.png")
    plt.close()
