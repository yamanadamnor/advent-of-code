import sys

list = []
# x = 0
# y = 0
tree_counter = 1 # Part 1 = 0, Part 2 = 1

list2 = [
    {
        "r": 1,
        "d": 1,
        "res": 0
    },
    {
        "r": 3,
        "d": 1,
        "res": 0
    },
    {
        "r": 5,
        "d": 1,
        "res": 0
    },
    {
        "r": 7,
        "d": 1,
        "res": 0
    },
    {
        "r": 1,
        "d": 2,
        "res": 0
    },
]

for line in sys.stdin:
    list.append(line)


# ----------- Part 1 -------------
# while y < len(list):
#     if list[y][x % 31] == "#":
#         tree_counter += 1

#     y += 1
#     x += 3


# ----------- Part 2 -------------
for slope in list2:
    y = 0
    x = 0
    # print(hej)
    while y < len(list):
        # print(x % 31, y)
        if list[y % len(list)][x % 31] == "#":
            slope["res"] += 1

        y += slope["d"]
        x += slope["r"]


for slope in list2:
    tree_counter *= slope["res"]
    # print(slope["res"])

print(tree_counter)