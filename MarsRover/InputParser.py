def parse_input(file_name):
    try:
        file = open(file_name, "r")

        max_x, max_y = [int(coordinate) for coordinate in file.readline().strip('\n').split(" ")]
        grid_size = (max_x, max_y)

        second_line = file.readline()
        start_x, start_y = [int(coordinate) for coordinate in second_line.strip('\n').split(" ")[:-1]]
        starting_coordinate = (start_x, start_y)
        starting_bearing = second_line.strip('\n').split(" ")[-1]
        starting_position = {"coordinate": starting_coordinate, "bearing": starting_bearing}

        command_sequence = [command for command in file.readline().strip('\n')]
    finally:
        file.close()
    return grid_size, starting_position, command_sequence
