def parse_input(file_name):
    try:
        file = open(file_name, "r")
        lines_of_input = [line.strip('\n') for line in file.readlines()]

        max_x, max_y = [int(coordinate) for coordinate in lines_of_input[0].split(" ")]
        grid_size = (max_x, max_y)

        start_x, start_y = [int(coordinate) for coordinate in lines_of_input[1].split(" ")[:-1]]
        starting_coordinate = (start_x, start_y)

        starting_bearing = lines_of_input[1].strip('\n').split(" ")[-1]
        starting_position = {"coordinate": starting_coordinate, "bearing": starting_bearing}

        command_sequence = [command for command in lines_of_input[2]]
    except IOError:
        print("IOError")
    finally:
        file.close()
    return grid_size, starting_position, command_sequence
