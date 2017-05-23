import unittest

from MarsRover.DangerousMoveException import DangerousMoveException
from MarsRover.Rover import Rover
from MarsRover.Zone import Zone


class RoverTest(unittest.TestCase):
    def setUp(self):
        self.safe_zone = Zone((2, 2))

    def test_move_north_increase_y_coordinate_of_position(self):
        rover = Rover((1, 1), "N", self.safe_zone)
        rover.move()
        self.assertEqual(rover.position, (1, 2))

    def test_move_east_increase_x_coordinate_of_position(self):
        rover = Rover((1, 1), "E", self.safe_zone)
        rover.move()
        self.assertEqual(rover.position, (2, 1))

    def test_move_south_decrease_y_coordinate_of_position(self):
        rover = Rover((1, 1), "S", self.safe_zone)
        rover.move()
        self.assertEqual(rover.position, (1, 0))

    def test_move_west_decrease_x_coordinate_of_position(self):
        rover = Rover((1, 1), "W", self.safe_zone)
        rover.move()
        self.assertEqual(rover.position, (0, 1))

    def test_move_north_into_danger_zone_throws_exception(self):
        with self.assertRaises(DangerousMoveException):
            rover = Rover((2, 2), "N", self.safe_zone)
            rover.move()
            self.fail("A DangerousMoveException should have been thrown")

    def test_move_east_into_danger_zone_throws_exception(self):
        with self.assertRaises(DangerousMoveException):
            rover = Rover((2, 2), "E", self.safe_zone)
            rover.move()
            self.fail("A DangerousMoveException should have been thrown")

    def test_move_south_into_danger_zone_throws_exception(self):
        with self.assertRaises(DangerousMoveException):
            rover = Rover((2, 0), "S", self.safe_zone)
            rover.move()
            self.fail("A DangerousMoveException should have been thrown")

    def test_move_west_into_danger_zone_throws_exception(self):
        with self.assertRaises(DangerousMoveException):
            rover = Rover((0, 2), "W", self.safe_zone)
            rover.move()
            self.fail("A DangerousMoveException should have been thrown")

    def test_turn_left_from_bearing_north_sets_bearing_west(self):
        rover = Rover((1, 1), "N", self.safe_zone)
        rover.turn_left()
        self.assertEqual(rover.bearing, "W")

    def test_turn_left_from_bearing_west_sets_bearing_south(self):
        rover = Rover((1, 1), "W", self.safe_zone)
        rover.turn_left()
        self.assertEqual(rover.bearing, "S")

    def test_turn_left_from_bearing_south_sets_bearing_east(self):
        rover = Rover((1, 1), "S", self.safe_zone)
        rover.turn_left()
        self.assertEqual(rover.bearing, "E")

    def test_turn_left_from_bearing_east_sets_bearing_north(self):
        rover = Rover((1, 1), "E", self.safe_zone)
        rover.turn_left()
        self.assertEqual(rover.bearing, "N")

    def test_turn_right_from_bearing_north_sets_bearing_east(self):
        rover = Rover((1, 1), "N", self.safe_zone)
        rover.turn_right()
        self.assertEqual(rover.bearing, "E")

    def test_turn_right_from_bearing_east_sets_bearing_south(self):
        rover = Rover((1, 1), "E", self.safe_zone)
        rover.turn_right()
        self.assertEqual(rover.bearing, "S")

    def test_turn_right_from_bearing_south_sets_bearing_west(self):
        rover = Rover((1, 1), "S", self.safe_zone)
        rover.turn_right()
        self.assertEqual(rover.bearing, "W")

    def test_turn_right_from_bearing_west_sets_bearing_north(self):
        rover = Rover((1, 1), "W", self.safe_zone)
        rover.turn_right()
        self.assertEqual(rover.bearing, "N")


if __name__ == '__main__':
    unittest.main()
