from MarsRover.InputParser import parse_input
from MarsRover.Rover import Rover
from MarsRover.Zone import Zone

if __name__ == '__main__':
    # TODO: handle file location in OS generic way
    instruction_file = "../example-input-file.txt"
    grid_size, starting_position, command_sequence = parse_input(instruction_file)
    rover_zone = Zone(grid_size)

    rover = Rover(starting_position["coordinate"], starting_position["bearing"], rover_zone)
    rover.save_command_sequence(command_sequence)
    rover.execute_command_sequence()
    rover.report_current_position()


