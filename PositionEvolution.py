from Position import Position


class PositionEvolution:
    def __init__(self, delta_t, box_size):
        self.delta_t = delta_t
        self.box_size = box_size

    def evolve_1_dimension(self, position_i, v_i):
        position_i_plus_1 = position_i + v_i * self.delta_t
        box_limit = self.box_size / 2

        if position_i_plus_1 > box_limit:
            position_i_plus_1 = position_i_plus_1 - self.box_size

        if position_i_plus_1 < -box_limit:
            position_i_plus_1 = position_i_plus_1 + self.box_size
        return position_i_plus_1

    def evolve(self, position_i, impulsion_i):
        position_i_plus_1_x = self.evolve_1_dimension(position_i.x, impulsion_i.v_x)
        position_i_plus_1_y = self.evolve_1_dimension(position_i.y, impulsion_i.v_y)
        return Position(position_i_plus_1_x, position_i_plus_1_y)
