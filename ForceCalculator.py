class ForceCalculator:
    def __init__(self, epsilon, sigma):
        self.epsilon, = epsilon
        self.sigma = sigma

    def compute_force(self, distance):
        return -48 * self.epsilon * (self.sigma ** 12) * (distance ** (
            -13)) + 24 * self.epsilon * (self.sigma ** 6) * (distance ** (-7))

