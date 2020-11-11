def main():
    try:
        location = input("Enter 1 to convert Nether Coords, Enter 2 to convert Overworld Coords: ")

        if location == '2' or location == '1':
            x = float(input("Enter your x value: "))
            y = float(input("Enter your y value: "))
            z = float(input("Enter your z value: "))

            # Converts Nether Coordinates to Overworld Coordinates
            if location == '1':
                netherCoords(x, y, z)
                main()

            # Converts Overworld Coordinates to Nether Coordinates
            elif location == '2':
                overworldCoords(x, y, z)
                main()
            else:
                print('Failed to convert Coords...')
        else:
            print('Please choose 1 or 2, no spaces or other characters allowed...')
            main()
    except Exception as e:
        print(e)


# Converts Nether Coordinates to Overworld Coordinates
def netherCoords(int1, int2, int3):
    try:
        int1 = int1 * 8.0
        int3 = int3 * 8.0
        print(f'Your converted coords are: {round(int1, 3)}, {round(int2, 3)}, {round(int3, 3)}')
    except Exception as e:
        print(e)
    # return int1, int2, int3


# Converts Overworld Coordinates to Nether Coordinates
def overworldCoords(int1, int2, int3):
    try:
        int1 = int1 // 8.0
        int3 = int3 // 8.0
        print(f'Your converted coords are: {round(int1, 3)}, {round(int2, 3)}, {round(int3, 3)}')
    except Exception as e:
        print(e)
    # return int1, int2, int3


main()
