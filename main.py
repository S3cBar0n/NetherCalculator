GREETING = """
====================================================
== Welcome to the Minecraft coordinate converter! ==
====================================================
""".strip("\n")

INPUT_INSTRUCTIONS = """
Enter 1 to convert Nether coordinates to Overworld coordinates
Enter 2 to convert Overworld coordinates to Nether coordinates
Enter e to exit the program
"""


def main():
    correct_input_provided = False
    # Handle incorrect inputs
    while not correct_input_provided:
        action = input(INPUT_INSTRUCTIONS)

        if action in ("1", "2"):
            correct_input_provided = True

            x_coordinate = get_coordinate("x")
            y_coordinate = get_coordinate("y")
            z_coordinate = get_coordinate("z")

            # Converts Nether Coordinates to Overworld Coordinates
            if action == '1':
                convert_to_overworld_coordinates(x_coordinate, y_coordinate, z_coordinate)

            # Converts Overworld Coordinates to Nether Coordinates
            elif action == '2':
                convert_to_nether_coordinates(x_coordinate, y_coordinate, z_coordinate)
        elif action in ("e", "E"):
            exit()
        else:
            print('\nIncorrect Input.')
    # Don't restart program instantly, wait for user to confirm
    if input('(Press <ENTER> to restart to program or "e" to exit) ') == "e":
        exit()


# Handle wrong coordinate inputs
def get_coordinate(coord_name: str):
    correct_input_provided = False
    coord_value = None
    while not correct_input_provided:
        try:
            coord_value = float(input(f"Enter your {coord_name} value: "))
        except ValueError:
            print("Incorrect input. Please enter a number.")
        else:
            correct_input_provided = True
    return coord_value


# Converts Nether Coordinates to Overworld Coordinates
def convert_to_overworld_coordinates(x_coord, y_coord, z_coord):
    x_coord = x_coord * 8.0
    z_coord = z_coord * 8.0
    print(f'Your converted coords are: {round(x_coord, 3)}, {round(y_coord, 3)}, {round(z_coord, 3)}')


# Converts Overworld Coordinates to Nether Coordinates
def convert_to_nether_coordinates(x_coord, y_coord, z_coord):
    overworld_x_coord = x_coord // 8.0
    overworld_z_coord = z_coord // 8.0
    print(f'Your converted coords are: {overworld_x_coord}, {y_coord}, {overworld_z_coord}')


if __name__ == '__main__':
    while True:
        print(GREETING)
        main()
