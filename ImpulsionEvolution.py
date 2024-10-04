from Impulsion import Impulsion


class ImpulsionEvolution:
    def __init__(self, delta_t):
        self.delta_t = delta_t

    def evolve_1_dimension_euler(self, v_i, force_i):
        return v_i + force_i * self.delta_t

    def evolve_euler(self, impulsion_i, force_i):
        v_i_plus_1_x = self.evolve_1_dimension_euler(impulsion_i.v_x, force_i.x)
        v_i_plus_1_y = self.evolve_1_dimension_euler(impulsion_i.v_y, force_i.y)
        return Impulsion(v_i_plus_1_x, v_i_plus_1_y)

    def evolve_1_dimension_velocity_verlet(self, v_i, force_i, force_i_plus_1):
        return v_i + 0.5 * (force_i + force_i_plus_1) * self.delta_t

    def evolve_velocity_verlet(self, impulsion_i, force_i, force_i_plus):
        v_i_plus_1_x = self.evolve_1_dimension_velocity_verlet(impulsion_i.v_x, force_i.x, force_i_plus.x)
        v_i_plus_1_y = self.evolve_1_dimension_velocity_verlet(impulsion_i.v_y, force_i.y, force_i_plus.y)
        return Impulsion(v_i_plus_1_x, v_i_plus_1_y)