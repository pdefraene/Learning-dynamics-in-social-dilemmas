import numpy as np


def bush_mosteller_chooser(probabilities):
    return np.random.choice([0, 1], p=probabilities)


def get_chooser_from_str(decision_heuristic):
    if decision_heuristic == "BM":
        return bush_mosteller_chooser


class DecisionModule:
    def __init__(self, decision_heuristic="BM", **kwargs):
        self.decision_heuristic = decision_heuristic
        self.create_decision = get_chooser_from_str(self.decision_heuristic)
        self.params = None  # TODO : this will contain the parameters, if any like tau or epsilon

    def choose(self, probabilities):
        # TODO : does a parameter need to be sent at every episode? Maybe aspiration or habituation
        return self.create_decision(probabilities)
