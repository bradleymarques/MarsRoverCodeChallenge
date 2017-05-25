import unittest

from MarsRover.Rover import Rover
from MarsRover.RoverController import RoverController
from MarsRover.Zone import Zone


class RoverControllerTest(unittest.TestCase):
    def test_is_command_sequence_safe_returns_true_for_safe_movement(self):
        rover = Rover((1, 1), "N", Zone((3, 3)))
        rover_controller = RoverController(rover)
        self.assertTrue(rover_controller.is_command_sequence_safe("MRM"))

    def test_is_command_sequence_safe_returns_false_for_unsafe_movement(self):
        rover = Rover((1, 1), "N", Zone((3, 1)))
        rover_controller = RoverController(rover)
        self.assertFalse(rover_controller.is_command_sequence_safe("M"))

if __name__ == '__main__':
    unittest.main()