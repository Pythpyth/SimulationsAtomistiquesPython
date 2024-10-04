import math

import numpy as np

from Impulsion import Impulsion
from ImpulsionEvolution import ImpulsionEvolution
from ParticleEvolution import ParticleEvolution
from Position import Position

import matplotlib.pyplot as plt

from PositionEvolution import PositionEvolution


class Simulation:
    @staticmethod
    def molecular_dynamic_simulation(time_step_number, time_end):
        m = 1
        epsilon = 1
        sigma = 1
        box_size = 6
        r_trunc = 2.5

        position_1 = Position(2.4, 1.8)
        position_2 = Position(1, 1)
        position_3 = Position(2, 2.3)
        position_4 = Position(-1, -2.8)

        impulsion_1 = Impulsion(0.001, 0.002)
        impulsion_2 = Impulsion(0.05, 0.03)
        impulsion_3 = Impulsion(-0.01, -0.03)
        impulsion_4 = Impulsion(-0.04, -0.07)

        position_i = [position_1, position_3]
        position_i_plus_1 = [position_1, position_3]
        impulsion_i = [impulsion_1, impulsion_3]
        impulsion_i_plus_1 = [impulsion_1, impulsion_3]

        nb_particle = len(position_i)

        time_step = time_end / time_step_number
        particle_evolution = ParticleEvolution(time_step, box_size, r_trunc)
        position_evolution = PositionEvolution(time_step, box_size)
        impulsion_evolution = ImpulsionEvolution(time_step)

        time_list = np.zeros(time_step_number + 1)
        total_energy = np.zeros(time_step_number + 1)
        positions_x = np.zeros(nb_particle)
        positions_y = np.zeros(nb_particle)

        for i in range(0, time_step_number):
            time_list[i + 1] = time_step * (i + 1)

            #evolution position
            for j in range(0, nb_particle):
                #positions_x[j] = particles_i[j].position.x
                #positions_y[j] = particles_i[j].position.y
                total_energy[i] += particle_evolution.compute_sum_cinetical_energy(impulsion_i[j])
                total_energy[i] += particle_evolution.compute_sum_potential_energy(position_i, j)

                force_i = particle_evolution.compute_sum_force(position_i, j)
                position_i_plus_1[j] = position_evolution.evolve_velocity_verlet(position_i[j], impulsion_i[j], force_i)

            #evolution impulsion et calcul des forces
            for j in range(0, nb_particle):
                force_i = particle_evolution.compute_sum_force(position_i, j)
                force_i_plus = particle_evolution.compute_sum_force(position_i_plus_1, j)
                impulsion_i_plus_1[j] = impulsion_evolution.evolve_velocity_verlet(impulsion_i[j], force_i,
                                                                                   force_i_plus)

            #remplace anciennes de données de position et impulsion par les nouvelles calculées
            for j in range(0, nb_particle):
                position_i[j] = position_i_plus_1[j]
                impulsion_i[j] = impulsion_i_plus_1[j]

        for j in range(0, nb_particle):
            total_energy[time_step_number] += particle_evolution.compute_sum_cinetical_energy(impulsion_i[j])
            total_energy[time_step_number] += particle_evolution.compute_sum_potential_energy(position_i, j)

        # plt.plot(time_list, total_energy, label='energy')
        # plt.xlabel('time')
        # plt.ylabel('total energy')
        # plt.legend()
        # plt.grid(True)
        # plt.show()


        return abs(total_energy[time_step_number] - total_energy[0])
        #file.close()

