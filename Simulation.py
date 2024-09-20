import numpy as np

from Impulsion import Impulsion
from Particle import Particle
from ParticleEvolution import ParticleEvolution
from Position import Position

import matplotlib.pyplot as plt


class Simulation:
    @staticmethod
    def molecular_dynamic_simulation(time_step_number, time_end):

        m = 1
        epsilon = 1
        sigma = 1
        particle_1 = Particle(Position(0, 0), Impulsion(0.001, 0.002))
        particle_2 = Particle(Position(1, 1), Impulsion( 0.05, 0.03))
        #particle_3 = Particle(Position(0.3, 0.7), Impulsion(-0.01, -0.03))
        nb_particle = 2
        particles = [particle_1, particle_2]
        time_step = time_end / time_step_number

        time_list = np.zeros(time_step_number)
        total_energy = np.zeros(time_step_number)
        particle_evolution = ParticleEvolution(time_step)
        #positions = [particle_1.position, particle_2.position, particle_3.position]
        positions_x = np.zeros(nb_particle)
        positions_y = np.zeros(nb_particle)

        for i in range(0, time_step_number):
            time_list[i] = time_step * i

            file = open('Coord\\positions_' + str(i) + ' .dat', "a")

            for j in range(0, nb_particle - 1):
                positions_x[j] = particles[j].position.x
                positions_y[j] = particles[j].position.y
                file.write('\n' + str(positions_x[j]) + ' ' + str(positions_y[j]))
                total_energy[i] += particle_evolution.compute_sum_cinetical_energy(particles[j])
                total_energy[i] += particle_evolution.compute_sum_potential_energy(particles, j)
                particles[j] = particle_evolution.evolve(particles, j)
            file.close()


        plt.plot(time_list, total_energy, label = 'energy')
        plt.xlabel('time')
        plt.ylabel('total energy')
        plt.legend()
        plt.grid(True)
        plt.show()






