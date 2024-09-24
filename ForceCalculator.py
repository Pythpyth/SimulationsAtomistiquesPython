from DistanceCalculator import DistanceCalculator
from Force import Force
from Position import Position


class ForceCalculator:
    def __init__(self, r_trunc, box_size):
        self.r_trunc = r_trunc
        self.box_size = box_size

    def get_shifted_position(self, position_1, position_2):
        #position1 reference : à voir
        distance_x = DistanceCalculator.compute_x_distance(position_1, position_2)
        distance_y = DistanceCalculator.compute_y_distance(position_1, position_2)

        position_2_shifted = Position(position_2.x, position_2.y)
        if distance_x > self.box_size / 2:
            position_2_shifted.x = position_2_shifted.x + self.box_size
        if distance_y > self.box_size / 2:
            position_2_shifted.y = position_2_shifted.y + self.box_size
        if distance_x < -self.box_size / 2:
            position_2_shifted.x = position_2_shifted.x - self.box_size
        if distance_y < -self.box_size / 2:
            position_2_shifted.y = position_2_shifted.y - self.box_size

        return position_2_shifted

    def compute_force(self, position_1, position_2):

        position_2_shifted = self.get_shifted_position(position_1, position_2)
        distance = DistanceCalculator.compute_distance(position_1, position_2_shifted)

        if distance > self.r_trunc:
            return Force(0.0, 0.0)
        else:
            x_multiplicative_factor = (position_1.x - position_2_shifted.x) / distance
            y_multiplicative_factor = (position_1.y - position_2_shifted.y) / distance

            common_factor = 48 * (distance ** (-13)) - 24 * (distance ** (-7))

            x_force = common_factor * x_multiplicative_factor
            y_force = common_factor * y_multiplicative_factor
            return Force(x_force, y_force)

    def compute_energy_pot(self, position_1, position_2):
        position_2_shifted = self.get_shifted_position(position_1, position_2)
        distance = DistanceCalculator.compute_distance(position_1, position_2_shifted)
        if distance > self.r_trunc:
            return 0.0
        else:
            return 4 * (((1.0 / distance) ** 12) - ((1.0 / distance) ** 6))
