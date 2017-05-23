import unittest

from MarsRover import InputParser


class TestInputParser(unittest.TestCase):
    def test_input_parser_finds_grid_size_in_file(self):
        grid_size, starting_position, command_sequence = InputParser.parse_input("example-input-file.txt")
        self.assertEqual(grid_size, (8, 8))

    def test_input_parser_finds_starting_position_in_file(self):
        grid_size, starting_position, command_sequence = InputParser.parse_input("example-input-file.txt")
        self.assertEqual(starting_position, {"coordinate": (1, 2), "bearing": "E"})

    def test_input_parser_finds_command_sequence_in_file(self):
        grid_size, starting_position, command_sequence = InputParser.parse_input("example-input-file.txt")
        self.assertEqual(command_sequence, [x for x in "MMLMRMMRRMML"])


if __name__ == "__main__":
    unittest.main()
