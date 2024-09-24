from DistanceCalculator import DistanceCalculator
from Force import Force
from ForceCalculator import ForceCalculator
from ImpulsionEvolution import ImpulsionEvolution
from Particle import Particle
from PositionEvolution import PositionEvolution


class ParticleEvolution:
    def __init__(self, delta_t, box_size, r_trunc):
        self.delta_t = delta_t
        self.box_size = box_size
        self.r_trunc = r_trunc
        self.position_evolution = PositionEvolution(self.delta_t, box_size)
        self.impulsion_evolution = ImpulsionEvolution(self.delta_t)

    def compute_sum_force(self, particles, index):

        force_calculator = ForceCalculator(self.r_trunc, self.box_size)
        force_result_x = 0
        force_result_y = 0

        for i in range(len(particles)):
            if i != index:
                force_i = force_calculator.compute_force(particles[index].position, particles[i].position)
                force_result_x += force_i.x
                force_result_y += force_i.y

        return Force(force_result_x, force_result_y)

    def compute_sum_potential_energy(self, particles, index):
        force_calculator = ForceCalculator(self.r_trunc, self.box_size)
        energy = 0

        for i in range(len(particles)):
            if i > index:
                energy += force_calculator.compute_energy_pot(particles[index].position, particles[i].position)

        return energy

    def compute_sum_cinetical_energy(self, particle):
        return 0.5 * (particle.impulsion.v_x ** 2 + particle.impulsion.v_y ** 2)

    def evolve(self, particles, index):
        force = self.compute_sum_force(particles, index)
        position_i_plus_1 = self.position_evolution.evolve(particles[index].position, particles[index].impulsion)
        impulsion_i_plus_1 = self.impulsion_evolution.evolve(particles[index].impulsion, force)
        return Particle(position_i_plus_1, impulsion_i_plus_1)