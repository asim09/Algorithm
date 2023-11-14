"16. Find the direction:"


def find_direction(commands, initial_pos):
    directions = ("N", "E", "S", "W")
    command_bounderies = ("L", "R")
    initial_pos_index = directions.index(initial_pos)
    print(initial_pos_index)
    counter = initial_pos_index
    for command in commands:
        if command in command_bounderies:
            counter = counter + -1 if command == "L" else 1
            new_position = directions[counter]
    return new_position


initial_pos = "S"
commands = "LLR L"
output = "W"
print(find_direction(commands, initial_pos))
