from Impulsion import Impulsion


class ImpulsionEvolution:
    def __init__(self, delta_t):
        self.delta_t = delta_t

    def evolve_1_dimension(self, v_i, force_i):
        return v_i + force_i * self.delta_t

    def evolve(self, impulsion_i, force_i):
        v_i_plus_1_x = self.evolve_1_dimension(impulsion_i.vx, force_i.x)
        v_i_plus_1_y = self.evolve_1_dimension(impulsion_i.vy, force_i.y)
        return Impulsion(v_i_plus_1_x, v_i_plus_1_y)
