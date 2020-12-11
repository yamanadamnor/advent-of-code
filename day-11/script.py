import sys
import itertools
from collections import Counter

my_list = []
history = []

for line in sys.stdin:
    my_list.append(list(line.strip()))


def get_adjecent(my_map, row, column):

    up = my_map[row-1][column]
    down = my_map[row+1][column]
    left = my_map[row][column-1]
    right = my_map[row][column-1]
    up_left = my_map[row-1][column-1]
    up_right= my_map[row-1][column+1]
    down_left = my_map[row+1][column-1]
    down_right = my_map[row+1][column+1]

    if (my_map[row][column] == "L" and up != "#" and down != "#" and left != "#"
            and right != "#" and up_left != "#" and up_right != "#"
            and down_left != "#" and down_right != "#"):

        my_map[row][column] = "#"
    # elif
    combs = Counter([up, down, left, right, up_left, up_right,
                     down_left, down_right])

    if combs["L"] >= 4:
        my_map[row][column] = "L"

    return my_map



def adjacent(my_map, row, column):

    adjacents = []

    if row > 0:
        up = my_map[row-1][column]
        adjacents.append(up)
        if column > 0:
            up_left = my_map[row-1][column-1]
            adjacents.append(up_left)
        if column + 1 < len(my_map[row]) -1:
            up_right= my_map[row-1][column+1]
            adjacents.append(up_right)


    if row+1 < len(my_map) - 1:
        down = my_map[row+1][column]
        adjacents.append(down)

        if column > 0:
            down_left = my_map[row+1][column-1]
            adjacents.append(down_left)
        if column + 1 < len(my_map[row]) -1:
            down_right = my_map[row+1][column+1]
            adjacents.append(down_right)

    if column > 0:
        left = my_map[row][column-1]
        adjacents.append(left)

    if column + 1 < len(my_map[row]) -1:
        right = my_map[row][column+1]
        adjacents.append(right)



    if row > 0 and column > 0:
        up_left = my_map[row-1][column-1]
        adjacents.append(up_left)


    return adjacents



# return (up, down, left, right, up_left, up_right, down_left, up_right)

# print(get_adjecent(my_list, 15, 55))

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        total = Counter(adjacent(my_list, i, j))
        if total["L"] + total["."] == 8:
        # history.append(adjacent(my_list, i, j))

totals = Counter(i for i in list(itertools.chain.from_iterable(my_list)))
print(totals)

