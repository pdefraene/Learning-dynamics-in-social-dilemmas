import numpy as np

# Action set = {C,D}
from DecisionModule import DecisionModule
from PayoffMatrix import PayoffMatrix


class Agent:
    def __init__(self, decision_heuristic='BM', nb_actions=2, learning_rate=1, aspiration_level=None,
                 habituation=None):  # TODO : find what value to start with for aspitation amd habituation
        self.probabilities = np.full(shape=nb_actions, fill_value=0.5, dtype=np.float64)
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
        # TODO : update other probabilities accordingly. So if p=[0.3, 0.6, 0.1] and p[0] goes from 0.3 to 0.6,
        #  0.4 will remain to be split : 0.4 * 0.6/0.7 for p[1] and 0.4 * 0.1/0.7 for p[2] T
        #  Or, since len(p) will always be 2, we can simply update the other p as the complementary prob of the one p
        return future_prob

    def update_aspiration(self, payoff):
        h = self.habituation
        A = self.aspiration_level
        A = (1 - h) * A + h * payoff
        self.aspiration_level = A
        return A

    def choose_action(self):
        return self.decision_maker.choose(self.probabilities)


if __name__ == '__main__':
    aspiration_level = 3.5
    agents = [Agent(aspiration_level=aspiration_level, habituation=0),
              Agent(aspiration_level=aspiration_level, habituation=0)]
    payoff_matrix = PayoffMatrix(5, 2, 6, 3)
    for i in range(100):
        first_choice = agents[0].choose_action()
        second_choice = agents[1].choose_action()
        payoff = payoff_matrix.get_payoff_for_actions_list((first_choice, second_choice))
        stimuli = [
            payoff_matrix.get_stimulus_for_payoff(payoff[0], agents[0].aspiration_level),
            payoff_matrix.get_stimulus_for_payoff(payoff[1], agents[1].aspiration_level)]
        agents[0].update_probabilities(stimuli[0], first_choice)
        agents[1].update_probabilities(stimuli[1], second_choice)

        agents[0].update_aspiration(payoff[0])
        agents[1].update_aspiration(payoff[1])
        for agent in agents:
            print(agent.probabilities, agent.aspiration_level)
