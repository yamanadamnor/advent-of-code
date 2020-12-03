import sys

list = []
correct = 0

for line in sys.stdin:
    list.append(line.split())

for el in list:
    el[0] = el[0].split("-")
    el[1] = el[1].split(":")[0]

for el in list:
    el[0][0] = int(el[0][0])
    el[0][1] = int(el[0][1])


# -------------- Part 1 ----------------
# for el in list:
#     counter = 0
#     for letter in el[2]:
#         if el[1] == letter:
#             counter += 1
#     if counter >= int(el[0][0]) and counter <= int(el[0][1]):
#         correct += 1


# -------------- Part 2 ----------------
for el in list:

    if el[2][el[0][0] - 1] == el[1] and el[2][el[0][1] - 1] != el[1]:
        correct += 1
    elif el[2][el[0][0] - 1] != el[1] and el[2][el[0][1] - 1] == el[1]:
        correct += 1


print(correct)