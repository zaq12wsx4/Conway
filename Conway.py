from random import randint
from turtle import *
from time import time

######################
# matrix[row(y)][column(x)]
# eg. matrix[1][3]:
# X X X X X X X X
# X X X O X X X X
# X X X X X X X X
# X X X X X X X X
######################

# create a matrix the size provided by x_len and y_len
# assign each variable in the matrix a random number, 0 or 1, to read from
x_len, y_len = 60, 60
matrix = [[randint(0, 1) for l in range(x_len)] for p in range(y_len)]

# make a hard copy of matrix for the rest of the program to write to
temp_matrix = [row[:] for row in matrix]
dot_size = 6

# set animation to false
tracer(False)
ht()

round_count = 0

# draw a new matrix of life and compute the next round
while True:
    start_time = time()
    # setup for turtle's position and clear the board
    penup()
    setpos(-x_len*(0.5*dot_size), y_len*(0.5*dot_size))
    clear()

    # draw a dot in a position for every int in matrix
    # runs for each row
    for i in range(y_len):
        # runs for each column
        for j in range(x_len):

            # test the int at the matrix current position, and draw a dot according to the reading
            if matrix[i][j] == 1:
                pencolor("black")
                dot(dot_size)
            else:
                pass

            # move the turtle incrementally to the right each round
            setx(xcor()+dot_size)

        # reset turtle x and move turtle down to the next line to draw
        setx(-x_len*(0.5*dot_size))
        sety(ycor()-dot_size)

    # checks the surroundings of all matrix items and adjusts matrix to predefined rules
    # runs for each row
    for i in range(y_len):
        #runs for each column
        for j in range(x_len):
            # set the surrounding live tile count to 0
            pos_count = 0
            # test each tile surrounding the tile
            # runs for each row
            for y in range(3):
                # runs for each column
                for x in range(3):
                    # try to test each position surrounding the tile, from top-left to bottom-right
                    # try in case of out of index error
                    try:
                        if (i + y-1) < 0 or (j + x-1) < 0:
                            raise IndexError()
                        # print(matrix[i + y-1][j + x-1])
                        if matrix[i + y-1][j + x-1] == 1:
                            pos_count = pos_count + 1
                    except IndexError:
                        pass

            # corrects for the above test function checking the tile for liveness
            if matrix[i][j] == 1:
                pos_count = pos_count - 1

            # covers rule 1 and rule 3
            if pos_count < 2 or pos_count > 3:
                temp_matrix[i][j] = 0

            # covers rule 2
            elif (pos_count == 3 or pos_count == 2) and matrix[i][j] == 1:
                pass

            # covers rule 4
            elif pos_count == 3:
                temp_matrix[i][j] = 1

    # make a hard copy of temp_matrix for the rest of the program to read from
    matrix = [row[:] for row in temp_matrix]

    # update the turtle drawing after making sure at least some time has passed since last update
    time_bool = True
    while time_bool:
        end_time = time()
        if (end_time - start_time) > 0.1:
            time_bool = False
    update()

    # print info on round number
    round_count = round_count + 1
    print("round", round_count)
