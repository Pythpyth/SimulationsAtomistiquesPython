from Impulsion import Impulsion
from Particle import Particle
from ParticleEvolution import ParticleEvolution
from Position import Position

import matplotlib.pyplot as plt


class Simulation:

    def molecular_dynamic_simulation(self, time_step_number, time_end):

        m = 1
        epsilon = 1
        sigma = 1
        particle_1 = Particle(Position(0, 0), Impulsion(m, 0, 0))
        particle_2 = Particle(Position(1, 1), Impulsion(m, 0, 0))
        particle_3 = Particle(Position(-2, -2), Impulsion(m, 0, 0))
        nb_particle = 3
        particles = [particle_1, particle_2, particle_3]
        time_step = time_end / time_step_number
        particle_evolution = ParticleEvolution(time_step)

        for i in range(0, time_step_number):
            for j in range(0, nb_particle - 1):
                particles[j] = particle_evolution.evolve(particles, j)





