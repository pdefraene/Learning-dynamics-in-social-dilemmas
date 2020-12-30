import numpy as np

from Agent import Agent
from PayoffMatrix import PayoffMatrix
from Plots import plot_probabilities_historic_average, plot_SRE_over_A


def ask_agents(agents):
    # VERY IMPORTANT to return a tuple otherwise numpy multiD access doesn't work as intended
    return tuple(ag.choose_action() for ag in agents)


def compute_stimuli(agents, payoffs, supremi):
    assert len(agents) == len(payoffs) == len(supremi)
    return [ag.compute_stimulus(payoffs[i], supremi[i]) for i, ag in enumerate(agents)]


def get_supremi(agents, payoff_matrix):
    assert len(agents) == len(payoff_matrix)
    return [payoff_matrix.get_supremum(ag.aspiration_level) for ag in agents]


def update_agents_probabilities(agents, stimuli, choices):
    assert len(agents) == len(stimuli) == len(choices)
    return [ag.update_probabilities(stimuli[i], choices[i]) for i, ag in enumerate(agents)]


def update_agents_aspiration(agents, payoffs):
    assert len(agents) == len(payoffs)
    return [ag.update_aspiration(payoffs[i]) for i, ag in enumerate(agents)]


def plot1():
    decision_heuristic = "BM"
    learning_rate = 0.5

    habituation = 0.2  # 0
    p_fill = 0.5

    aspiration_level = 0.5  # 0.5  2  3.5
    Prisoners_Dilemma_values = [1, 3, 0, 4]
    Chicken_Game_values = [0, 3, 1, 4]
    Stag_Hunt_values = [1, 4, 0, 3]

    nb_agents = 2
    nb_actions = 2

    nb_rep = 1
    nb_ep = 500  # 100

    probabilities_historic = np.zeros((3, nb_ep), dtype=np.float64)
    for j, game in enumerate([Prisoners_Dilemma_values, Chicken_Game_values, Stag_Hunt_values]):
        payoff_matrix_main = PayoffMatrix(*game)
        for rep in range(nb_rep):
            agents_main = [Agent(decision_heuristic, learning_rate, aspiration_level, habituation, p_fill) for _ in range(nb_agents)]
            print(f"Calculating {rep}/{nb_rep}", end="\r")
            for t in range(nb_ep):
                choices_main = ask_agents(agents_main)
                payoffs_main = payoff_matrix_main.get_payoff_for_actions_list(choices_main)
                supremi_main = get_supremi(agents_main, payoff_matrix_main)
                stimuli_main = compute_stimuli(agents_main, payoffs_main, supremi_main)
                new_proba_main = update_agents_probabilities(agents_main, stimuli_main, choices_main)
                new_aspi_main = update_agents_aspiration(agents_main, payoffs_main)

                probabilities_historic[(j, t)] += new_proba_main[0][0]
    probabilities_historic /= nb_rep
    plot_probabilities_historic_average(probabilities_historic)


def plot2():
    decision_heuristic = "BM"
    learning_rate = 0.5
    habituation = 0
    p_fill = 0.5
    nb_agents = 2
    nb_actions = 2
    nb_rep = 250  # 250
    nb_ep = 1000  # 1000

    SRE_probabilities = np.zeros((3, 3, 40), dtype=np.float64)  # , nb_rep, nb_ep, nb_agents, nb_actions)
    for i, (fear, greed) in enumerate([(0, 4), (-1, 4), (0, 5)]):  # classic, fear, greed
        prisoners_dilemma = [1, 3, fear, greed]  # [p, r, s, t]
        chicken_game = [0, 3, 1, greed]
        stag_hunt = [1, 4, fear, 3]
        for j, game in enumerate([prisoners_dilemma, chicken_game, stag_hunt]):
            if j == 0 or i != j:
                payoff_matrix_main = PayoffMatrix(*game)
                for A0 in range(40):
                    for rep in range(nb_rep):
                        agents_main = [Agent(decision_heuristic, learning_rate, A0 / 10, habituation, p_fill) for _ in
                                       range(nb_agents)]
                        print(f"Calculating {rep}/{nb_rep} for A {A0 / 10} and game {j + 1}  ", end="\r")
                        for _ in range(nb_ep):
                            choices_main = ask_agents(agents_main)
                            payoffs_main = payoff_matrix_main.get_payoff_for_actions_list(choices_main)
                            supremi_main = get_supremi(agents_main, payoff_matrix_main)
                            stimuli_main = compute_stimuli(agents_main, payoffs_main, supremi_main)
                            new_proba_main = update_agents_probabilities(agents_main, stimuli_main, choices_main)
                            new_aspi_main = update_agents_aspiration(agents_main, payoffs_main)
                            if new_proba_main[0][0] >= 0.999:
                                SRE_probabilities[(j, i, A0)] += 1
    SRE_probabilities /= nb_rep
    SRE_probabilities /= nb_ep
    plot_SRE_over_A(SRE_probabilities)


if __name__ == '__main__':
    plot2()
