from cube import Cube


def main():

    inputs = ["superfl!p: UR2FBRB2RU2LB2RU'D'R2FR'LB2U2F2", "", "U", "Ui", "U2", "L'", "R", "U2 L' D"]
    #inputs = [""]
    for input in inputs:
        cube = Cube()
        cube.rotate(input)
        print('grade',cube.grade())
        print(input)
        print(cube)


if __name__ == '__main__':
    main()

