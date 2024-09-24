import unittest

from ForceCalculator import ForceCalculator
from Position import Position


class MyTestCase(unittest.TestCase):
    def test_something(self):
        epsilon = 1e-5
        position_1 = Position(-0.3, 0.2)
        position_2 = Position(0.5, 0.8)
        box_size = 6
        r_trunc = 2.5
        force_calculator = ForceCalculator(r_trunc, box_size)

        position_1_x_plus_epsilon = Position(position_1.x + epsilon, position_1.y)
        position_1_x_minus_epsilon = Position(position_1.x - epsilon, position_1.y)

        position_1_y_plus_epsilon = Position(position_1.x, position_1.y + epsilon)
        position_1_y_minus_epsilon = Position(position_1.x, position_1.y - epsilon)

        force = force_calculator.compute_force(position_1, position_2)

        x_force_recomputed = (-(force_calculator.compute_energy_pot(position_1_x_plus_epsilon, position_2) -
                                force_calculator.compute_energy_pot(position_1_x_minus_epsilon, position_2))
                              / (2 * epsilon))

        y_force_recomputed = (-(force_calculator.compute_energy_pot(position_1_y_plus_epsilon, position_2) -
                                force_calculator.compute_energy_pot(position_1_y_minus_epsilon, position_2)) /
                              (2 * epsilon))

        self.assertLess(abs(force.x - x_force_recomputed), 1e-7)
        self.assertLess(abs(force.y - y_force_recomputed), 1e-7)
