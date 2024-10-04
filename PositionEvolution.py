from Position import Position


class PositionEvolution:
    def __init__(self, delta_t, box_size):
        self.delta_t = delta_t
        self.box_size = box_size

    def apply_boundary_condition(self, position_i):
        box_limit = self.box_size / 2
        position_i = position_i % self.box_size
        if position_i > box_limit:
            return position_i - self.box_size
        if position_i < -box_limit:
            return position_i + self.box_size

        return position_i

    def evolve_1_dimension_euler(self, position_i, v_i):
        position_i_plus_1 = position_i + v_i * self.delta_t
        return self.apply_boundary_condition(position_i_plus_1)

    def evolve_1_dimension_velocity_verlet(self, position_i, v_i, force_i):
        position_i_plus_1 = position_i + v_i * self.delta_t + 0.5 * force_i * self.delta_t ** 2
        return self.apply_boundary_condition(position_i_plus_1)

    def evolve_euler(self, position_i, impulsion_i):
        position_i_plus_1_x = self.evolve_1_dimension_euler(position_i.x, impulsion_i.v_x)
        position_i_plus_1_y = self.evolve_1_dimension_euler(position_i.y, impulsion_i.v_y)
        return Position(position_i_plus_1_x, position_i_plus_1_y)

    def evolve_velocity_verlet(self, position_i, impulsion_i, force_i):
        position_i_plus_1_x = self.evolve_1_dimension_velocity_verlet(position_i.x, impulsion_i.v_x, force_i.x)
        position_i_plus_1_y = self.evolve_1_dimension_velocity_verlet(position_i.y, impulsion_i.v_y, force_i.y)
        return Position(position_i_plus_1_x, position_i_plus_1_y)