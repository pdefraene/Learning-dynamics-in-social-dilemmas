import numpy as np

from DecisionModule import DecisionModule


class Agent:
    def __init__(self, decision_heuristic='BM', learning_rate=0.5, aspiration_level=2,
                 habituation=0, probabilities_init=0.5):
        self.probabilities = np.full(shape=2, fill_value=probabilities_init, dtype=np.float64)
        self.learning_rate = learning_rate
        self.aspiration_level = aspiration_level
        self.habituation = habituation

        self.decision_maker = DecisionModule(decision_heuristic)

    def update_probabilities(self, stimulus, action):
        p = self.probabilities[action]
        l = self.learning_rate
        if stimulus >= 0:
            future_prob = p + (1 - p) * l * stimulus
        else:
            future_prob = p + p * l * stimulus
        self.probabilities[action] = future_prob
        self.probabilities[1 - action] = 1 - future_prob
        return self.probabilities

    def update_aspiration(self, payoff):
        h = self.habituation
        A = self.aspiration_level
        A = (1 - h) * A + h * payoff
        self.aspiration_level = A
        return A

    def choose_action(self):
        return self.decision_maker.choose(self.probabilities)

    def compute_stimulus(self, payoff, supremum):
        return (payoff - self.aspiration_level) / supremum


