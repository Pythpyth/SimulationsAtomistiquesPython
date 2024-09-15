class DistanceCalculator:
    @staticmethod
    def compute_distance(position_1, position_2):
        return (((position_1.x - position_2.x) ** 2) + ((position_1.y - position_2.y) ** 2)) ** 0.5
