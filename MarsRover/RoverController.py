from MarsRover.DangerousMoveException import DangerousMoveException
from MarsRover.Rover import Rover


class RoverController:
    def __init__(self, rover):
        self.rover = rover
        self.command_sequence = []

    def simulate_rover_movement(self):
        is_command_sequence_safe = True
        rover_sim = Rover(self.rover.position, self.rover.bearing, self.rover.safeZone)
        rover_sim.save_command_sequence(self.command_sequence)

        try:
            rover_sim.execute_command_sequence()
        except DangerousMoveException:
            is_command_sequence_safe = False

        return is_command_sequence_safe

    def is_command_sequence_safe(self, command_sequence):
        self.command_sequence = command_sequence
        return self.simulate_rover_movement()

    def transmit_command_sequence_to_rover(self, command_sequence):
        if self.is_command_sequence_safe(command_sequence):
            self.rover.save_command_sequence(command_sequence)

    def instruct_rover_to_execute_command_sequence(self):
        self.rover.execute_command_sequence()
        self.rover.report_current_position()
