import numpy as np


# Action set = {C,D}
from DecisionModule import DecisionModule


class Agent:
    def __init__(self, decision_heuristic='BM', nb_actions=2, learning_rate=1, aspiration_level=None, habituation=None):  # TODO : find what value to start with for aspitation amd habituation
        self.probabilities = np.empty(nb_actions, dtype=np.float64)
        self.learning_rate = learning_rate
        self.aspiration_level = aspiration_level
        self.habituation = habituation

        self.decision_maker = DecisionModule(decision_heuristic)

    def update_probabilities(self, stimulus, action):
        p = self.probabilities[action]
        l = self.learning_rate
        if stimulus >= 0:
            future_prob = p + (1-p)*l*stimulus
        else:
            future_prob = p + p*l*stimulus
        self.probabilities[action] = future_prob
        # TODO : update other probabilities accordingly. So if p=[0.3, 0.6, 0.1] and p[0] goes from 0.3 to 0.6,
        #  0.4 will remain to be split : 0.4 * 0.6/0.7 for p[1] and 0.4 * 0.1/0.7 for p[2] T
        #  Or, since len(p) will always be 2, we can simply update the other p as the complementary prob of the one p
        return future_prob

    def update_aspiration(self, payoff):
        h = self.habituation
        A = self.aspiration_level
        A = (1-h)*A + h*payoff
        self.aspiration_level = A
        return A

    def choose_action(self):
        return self.decision_maker.choose()