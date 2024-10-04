import math
import unittest

import numpy as np
import scipy
from matplotlib import pyplot as plt

from Simulation import Simulation


class MyTestCase(unittest.TestCase):

    def test_something(self):
        time_step_numbers = [1000, 5000, 10000, 50000, 100000, 200000]
        #time_step_numbers = [800000]
        ln_time_step = np.zeros(len(time_step_numbers))
        ln_delta_energy = np.zeros(len(time_step_numbers))
        time_end = 10
        simulation = Simulation
        for i in range(0, len(time_step_numbers)):
            time_step = time_end / time_step_numbers[i]
            ln_time_step[i] = math.log(time_step)
            ln_delta_energy[i] = math.log(simulation.molecular_dynamic_simulation(time_step_numbers[i], time_end))

        linear_regression = scipy.stats.linregress(ln_time_step, ln_delta_energy)
        print('slope = ' + str(linear_regression.slope))
        print('R = ' + str(linear_regression.rvalue))

        plt.scatter(ln_time_step, ln_delta_energy, label='ln|energy(t=0.5) - energy(t=0)|')
        plt.xlabel('ln(delta t)')
        plt.ylabel('ln(|energy(t=0.5) - energy(t=0)|)')
        plt.legend()
        plt.grid(True)
        plt.show()