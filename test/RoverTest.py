import unittest

from MarsRover.Rover import Rover


class RoverTest(unittest.TestCase):
    def test_move_north_increase_y_coordinate_of_position(self):
        rover = Rover((1, 1), "N")
        rover.move()
        self.assertEqual(rover.position, (1, 2))

    def test_move_east_increase_x_coordinate_of_position(self):
        rover = Rover((1, 1), "E")
        rover.move()
        self.assertEqual(rover.position, (2, 1))

    def test_move_south_decrease_y_coordinate_of_position(self):
        rover = Rover((1, 1), "S")
        rover.move()
        self.assertEqual(rover.position, (1, 0))

    def test_move_west_decrease_x_coordinate_of_position(self):
        rover = Rover((1, 1), "W")
        rover.move()
        self.assertEqual(rover.position, (0, 1))


if __name__ == '__main__':
    unittest.main()
