from DistanceCalculator import DistanceCalculator
from Force import Force


class ForceCalculator:
    def compute_force(self, position_1, position_2):
        distance = DistanceCalculator.compute_distance(position_1, position_2)
        x_multiplicative_factor = (position_1.x - position_2.x) / distance
        y_multiplicative_factor = (position_1.y - position_2.y) / distance

        common_factor = 48 * (distance ** (-13)) - 24 * (distance ** (-7))

        x_force = common_factor * x_multiplicative_factor
        y_force = common_factor * y_multiplicative_factor
        return Force(x_force, y_force)

    def compute_energy_pot(self, position_1, position_2):
        distance = DistanceCalculator.compute_distance(position_1, position_2)

        return 4 * (((1.0 / distance) ** 12) - ((1.0 / distance) ** 6))
