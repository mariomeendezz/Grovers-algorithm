import matplotlib.pyplot as plt

def plot_complexities(N: int=100):
    """
    Plots the time complexities O(N) and O(√N) for input sizes from 1 to N.
    """
    o_n = [i for i in range(1, N+1)]
    o_sqrt_n = [i**0.5 for i in o_n]

    plt.plot(o_n, label='O(N)')
    plt.plot(o_sqrt_n, label='O(√N)')
    plt.xlabel('Input Size (N)')
    plt.ylabel('Time Complexity')
    plt.title('Comparison of O(N) and O(√N) Time Complexities')
    plt.legend()
    plt.show()