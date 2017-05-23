class Zone:
    def __init__(self, max_coordinate):
        self.max_coordinate = max_coordinate

    def is_coordinate_in_safe_zone(self, coordinate):
        x_coordinate_is_between_zero_and_max_x = 0 <= coordinate[0] <= self.max_coordinate[0]
        y_coordinate_is_between_zero_and_max_y = 0 <= coordinate[1] <= self.max_coordinate[1]
        return x_coordinate_is_between_zero_and_max_x and y_coordinate_is_between_zero_and_max_y
