class DangerousMoveException(Exception):
    """Rover was instructed to move out of the safe zone"""

    def __init__(self, current_position, safe_zone, unsafe_position):
        self.current_position = current_position
        self.safe_zone = safe_zone
        self.unsafe_position = unsafe_position