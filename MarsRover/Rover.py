class Rover:
    def __init__(self, position, bearing):
        self.position = position
        self.bearing = bearing

    def move(self):
        if self.bearing == "N":
            self.position = (self.position[0], self.position[1] + 1)

        elif self.bearing == "E":
            self.position = (self.position[0] + 1, self.position[1])

        elif self.bearing == "S":
            self.position = (self.position[0], self.position[1] - 1)

        elif self.bearing == "W":
            self.position = (self.position[0] - 1, self.position[1])

    def turn_left(self):
        if self.bearing == "N":
            self.bearing = "W"

        elif self.bearing == "W":
            self.bearing = "S"

        elif self.bearing == "S":
            self.bearing = "E"

        elif self.bearing == "E":
            self.bearing = "N"
