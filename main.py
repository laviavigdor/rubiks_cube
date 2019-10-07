from cube import Cube, POSSIBLE_MOVES, UNDO_MOVE
from random import randrange, choice, seed
seed( 30 )


def main():
    cube = Cube()

    moves = [choice(POSSIBLE_MOVES) for _ in range(10)]
    for move in moves:
        cube.rotate(move)
        print(cube.get_slim_representation())
        print(cube)
    #     print(' ')
    #     # print(cube.grade())

    # print(cube)
    # print('---')
    # for move in [UNDO_MOVE[move] for move in list(reversed(moves))]:
    #     cube.rotate(move)
    #     # print(cube.grade())
    #
    # print(cube)
    # print(moves)
    # for input in inputs:
    #     cube = Cube()
    #     cube.rotate(input)
    #     print('grade',cube.grade())
    #     print(input)
    #     print(cube)


if __name__ == '__main__':
    main()

