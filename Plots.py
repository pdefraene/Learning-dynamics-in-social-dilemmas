import numpy as np
import sys
import matplotlib.pyplot as plt
np.set_printoptions(threshold=sys.maxsize)
plt.rc("font", **{"size" : 20})


def plot_probabilities_historic_average(historic, nb_rep, values, aspiration_level, l, h, p, game):
    Prisoners_Dilemma_values = [[1, 3, 0, 4], 2]
    Chicken_Game_values = [[0, 3, 1, 4], 2]
    Stag_Hunt_values = [[1, 4, 0, 3], 2]

    title = ""
    #if nb_rep != 1:
    #    title = f"Average over {nb_rep} of "
    #if game == Prisoners_Dilemma_values:
    #    title += f"Prisoner's Dilemma with\nT={values['T']} > R={values['R']} > A0={aspiration_level} > P={values['P']} > S={values['S']}"
    #elif game == Chicken_Game_values:
    #    title += f"Chicken Game with\nT={values['T']} > R={values['R']} > A0={aspiration_level} > S={values['S']} > P={values['P']}"
    #elif game == Stag_Hunt_values:
    #    title += f"Stag Hunt with\nR={values['R']} > T={values['T']} > A0={aspiration_level} > P={values['P']} > S={values['S']}"
    #title += f"\nl={l}, h={h}, pC0={p}"
    historic = np.mean(historic, axis=0)

    first_agent_first_proba = np.empty(len(historic), dtype=np.float64)

    for i in range(len(historic)):
        first_agent_first_proba[i] = historic[i][0][0]

    f, ax = plt.subplots(1)
    ax.plot(first_agent_first_proba)
    ax.set_ylim(ymin=0, ymax=1)
    ax.spines["top"].set_visible(False)
    plt.ylabel("Cooperation rate")
    plt.xlabel("iteration")

    plt.title(title)
    plt.show()

def plot_SRE_over_A(data):
    games_names = ["prisoners dilemma", "chicken", "stag hunt"]
    x = np.linspace(0, 4, 40)
    for game in range(len(data)):
        plt.subplot(3, 1, game+1)
        plt.ylim(0, 1.1)
        plt.plot(x, data[game][0])
        plt.title(games_names[game]+" game")
    plt.show()

    for game in range(len(data)):
        plt.subplot(3, 1, game+1)
        plt.ylim(0, 1.1)
        plt.plot(x, data[game][0], color='black', linestyle='dashed', label='classic', alpha=0.6)
        if game != 2:
            plt.plot(x, data[game][1], color='red', label='greed', alpha=0.6)
        if game != 1:
            plt.plot(x, data[game][2], color='blue', label='fear', alpha=0.6)
        plt.title(games_names[game]+" game")
        plt.legend()
    plt.show()
