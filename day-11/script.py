import sys
import itertools
from collections import Counter
from copy import deepcopy

my_list = []

for line in sys.stdin:
    my_list.append(list(line.strip()))


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


    if row+1 <= len(my_map) - 1:
        down = my_map[row+1][column]
        adjacents.append(down)

        if column > 0:
            down_left = my_map[row+1][column-1]
            adjacents.append(down_left)
        if column + 1 <= len(my_map[row]) -1:
            down_right = my_map[row+1][column+1]
            adjacents.append(down_right)

    if column > 0:
        left = my_map[row][column-1]
        adjacents.append(left)

    if column + 1 <= len(my_map[row]) -1:
        right = my_map[row][column+1]
        adjacents.append(right)

    return adjacents


# while True:
for i in range(2):
    hej_list = deepcopy(my_list)

    for i, row in enumerate(my_list):
        for j, column in enumerate(my_list):

            amount_of_adj = len(adjacent(my_list, i, j))
            total = Counter(adjacent(my_list, i, j))

            print(total)
            print("#" not in total.keys())
            if my_list[i][j] == "L" and "#" not in total.keys():
                hej_list[i][j] = "#"

            elif my_list[i][j] == "#" and total["#"] <= 4:
                hej_list[i][j] = "L"

    if my_list == hej_list:
        break

    my_list = deepcopy(hej_list)



for i in my_list:
    print(i)
totals = Counter(i for i in list(itertools.chain.from_iterable(my_list)))
print(totals)
