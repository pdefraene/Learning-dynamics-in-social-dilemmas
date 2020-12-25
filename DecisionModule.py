def bush_mosteller_chooser():
    pass  # TODO implement the decision making


def get_chooser_from_str(decision_heuristic, **kwargs):
    if decision_heuristic == "BM":
        return bush_mosteller_chooser


class DecisionModule:
    def __init__(self, decision_heuristic="BM", **kwargs):
        self.decision_heuristic = decision_heuristic
        self.create_decision = get_chooser_from_str(self.decision_heuristic, **kwargs)

    def choose(self):  # TODO : do not forget to add correct arguments
        return self.create_decision()
