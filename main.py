from MarsRover.InputParser import parse_input
from MarsRover.Rover import Rover
from MarsRover.Zone import Zone
from MarsRover.RoverController import RoverController

if __name__ == '__main__':
    # TODO: handle file location in OS generic way
    instruction_file = "example-input-file.txt"
    grid_size, starting_position, command_sequence = parse_input(instruction_file)

    rover_zone = Zone(grid_size)
    rover = Rover(starting_position["coordinate"], starting_position["bearing"], rover_zone)

    rover_controller = RoverController(rover)
    rover_controller.transmit_command_sequence_to_rover(command_sequence)
    rover_controller.instruct_rover_to_execute_command_sequence()
