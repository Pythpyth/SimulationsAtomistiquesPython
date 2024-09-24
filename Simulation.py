import math

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
        box_size = 6
        r_trunc = 2.5
        #particle_1 = Particle(Position(0, 0),Impulsion(0.001, 0.002))
        #particle_2 = Particle(Position(0.8, 0.7), Impulsion(0.05, 0.03))
        particle_1 = Particle(Position(0, 0), Impulsion(0.001, 0.002))
        particle_2 = Particle(Position(1, 1), Impulsion(0.05, 0.03))
        particle_3 = Particle(Position(2, 2.3), Impulsion(-0.01, -0.03))
        particle_4 = Particle(Position(-1, -2.8), Impulsion(-0.04, -0.07))

        particles_i = [particle_1, particle_2, particle_3, particle_4]
        nb_particle = len(particles_i)
        particles_i_plus_1 = [particle_1, particle_2, particle_3, particle_4]
        time_step = time_end / time_step_number
        particle_evolution = ParticleEvolution(time_step, box_size, r_trunc)

        time_list = np.zeros(time_step_number + 1)
        total_energy = np.zeros(time_step_number + 1)
        positions_x = np.zeros(nb_particle)
        positions_y = np.zeros(nb_particle)

        for i in range(0, time_step_number):
            time_list[i + 1] = time_step * (i + 1)
            #file = open('Coord\\positions_' + str(i) + ' .dat', "a")
            for j in range(0, nb_particle):
                positions_x[j] = particles_i[j].position.x
                positions_y[j] = particles_i[j].position.y
                total_energy[i] += particle_evolution.compute_sum_cinetical_energy(particles_i[j])
                total_energy[i] += particle_evolution.compute_sum_potential_energy(particles_i, j)
                particles_i_plus_1[j] = particle_evolution.evolve(particles_i, j)
                #file.write('\n' + str(positions_x[j]) + ' ' + str(positions_y[j]))

            for j in range(0, nb_particle):
                particles_i[j] = particles_i_plus_1[j]

        for j in range(0, nb_particle):
            total_energy[time_step_number] += particle_evolution.compute_sum_cinetical_energy(particles_i[j])
            total_energy[time_step_number] += particle_evolution.compute_sum_potential_energy(particles_i, j)

        # plt.plot(time_list, total_energy, label='energy')
        # plt.xlabel('time')
        # plt.ylabel('total energy')
        # plt.legend()
        # plt.grid(True)
        # plt.show()


        return abs(total_energy[time_step_number] - total_energy[0])
        #file.close()

