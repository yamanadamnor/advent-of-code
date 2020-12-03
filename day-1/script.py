import sys

list = []

for i in sys.stdin:
    list.append(int(i))

#------------------ Part 1 -------------------

# for i in list:
#     for j in list:
#         if (j + i) == 2020:
#             print(i * j)

#------------------ Part 2 -------------------

for i in list:
    for j in list:
        for m in list:
            if (j + i + m) == 2020:
                print(i * j * m)