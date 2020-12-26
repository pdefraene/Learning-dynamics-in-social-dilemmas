import numpy as np


def bush_mosteller_chooser():
    return np.random.randint(0,1)
    # TODO implement the decision making


def get_chooser_from_str(decision_heuristic):
    if decision_heuristic == "BM":
        return bush_mosteller_chooser


class DecisionModule:
    def __init__(self, decision_heuristic="BM", **kwargs):
        self.decision_heuristic = decision_heuristic
        self.create_decision = get_chooser_from_str(self.decision_heuristic)
        self.params = None  # TODO : this will contain the parameters, if any like tau or epsilon

    def choose(self, current_episode_information):  # TODO : does a parameter need to be sent at every episode? Maybe aspiration or habituation
        return self.create_decision()
