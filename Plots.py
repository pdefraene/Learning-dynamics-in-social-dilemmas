import numpy as np
import sys
import matplotlib.pyplot as plt
np.set_printoptions(threshold=sys.maxsize)
plt.rc("font", **{"size" : 20})


def plot_probabilities_historic_average(historic):
    games_names = ["prisoners dilemma", "chicken", "stag hunt"]
    for game in range(len(historic)):
        plt.subplot(3, 1, game+1)
        plt.ylim(0, 1.1)
        plt.title(games_names[game]+" game")
        plt.ylabel("Cooperation rate")
        if game == 2:
            plt.xlabel("iteration")
        plt.plot(historic[game])
    plt.show()


def plot_SRE_over_A(data):
    games_names = ["prisoners dilemma", "chicken", "stag hunt"]
    x = np.linspace(0, 4, 40)
    for game in range(len(data)):
        plt.subplot(3, 1, game+1)
        plt.ylim(0, 1.1)
        plt.title(games_names[game]+" game")
        if game == 1:
            plt.ylabel("SRE rate")
        if game == 2:
            plt.xlabel("A0")
        plt.plot(x, data[game][0])
    plt.show()

    for game in range(len(data)):
        plt.subplot(3, 1, game+1)
        plt.ylim(0, 1.1)
        plt.plot(x, data[game][0], color='black', linestyle='dashed', label='classic', alpha=0.6)
        if game != 1:
            plt.plot(x, data[game][1], color='blue', label='fear', alpha=0.6)
        if game != 2:
            plt.plot(x, data[game][2], color='red', label='greed', alpha=0.6)
        plt.title(games_names[game]+" game")
        if game == 1:
            plt.ylabel("SRE rate")
        if game == 2:
            plt.xlabel("A0")
        plt.legend()
    plt.show()
