import unittest

from Simulation import Simulation


class MyTestCase(unittest.TestCase):


    def test_something(self):
        time_step_number = 100
        time_end = 3.0
        simulation = Simulation
        simulation.molecular_dynamic_simulation(time_step_number, time_end)

