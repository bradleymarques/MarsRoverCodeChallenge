from MarsRover.DangerousMoveException import DangerousMoveException


class Rover:
    def __init__(self, position, bearing, safe_zone):
        self.position = position
        self.bearing = bearing
        self.safeZone = safe_zone

    def is_position_safe(self, position):
        return self.safeZone.is_coordinate_in_safe_zone(position)

    def move(self):
        if self.bearing == "N":
            next_position = (self.position[0], self.position[1] + 1)

        elif self.bearing == "E":
            next_position = (self.position[0] + 1, self.position[1])

        elif self.bearing == "S":
            next_position = (self.position[0], self.position[1] - 1)

        elif self.bearing == "W":
            next_position = (self.position[0] - 1, self.position[1])

        if not self.is_position_safe(next_position):
            raise DangerousMoveException(self.position, self.safeZone, next_position)
        self.position = next_position

    def turn_left(self):
        if self.bearing == "N":
            self.bearing = "W"

        elif self.bearing == "W":
            self.bearing = "S"

        elif self.bearing == "S":
            self.bearing = "E"

        elif self.bearing == "E":
            self.bearing = "N"

    def turn_right(self):
        if self.bearing == "N":
            self.bearing = "E"

        elif self.bearing == "E":
            self.bearing = "S"

        elif self.bearing == "S":
            self.bearing = "W"

        elif self.bearing == "W":
            self.bearing = "N"
