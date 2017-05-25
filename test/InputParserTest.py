import unittest

from MarsRover import InputParser


class TestInputParser(unittest.TestCase):
    def setUp(self):
        file_name = "example-input-file.txt"
        self.grid_size, self.starting_position, self.command_sequence = InputParser.parse_input(file_name)

    def test_input_parser_finds_grid_size_in_file(self):
        self.assertEqual(self.grid_size, (8, 8))

    def test_input_parser_finds_starting_position_in_file(self):
        self.assertEqual(self.starting_position, {"coordinate": (1, 2), "bearing": "E"})

    def test_input_parser_finds_command_sequence_in_file(self):
        self.assertEqual(self.command_sequence, [x for x in "MMLMRMMRRMML"])


if __name__ == "__main__":
    unittest.main()
