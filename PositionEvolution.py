from Position import Position


class PositionEvolution:
    def __init__(self, delta_t):
        self.delta_t = delta_t

    def evolve_1_dimension(self, position_i, v_i):
        return position_i + v_i * self.delta_t

    def evolve(self, position_i, impulsion_i):
        position_i_plus_1_x = self.evolve_1_dimension(position_i.x, impulsion_i.vx)
        position_i_plus_1_y = self.evolve_1_dimension(position_i.y, impulsion_i.vy)
        return Position(position_i_plus_1_x, position_i_plus_1_y)
