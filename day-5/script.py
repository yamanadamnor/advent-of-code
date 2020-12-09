import sys

list = []

for line in sys.stdin:
    list.append(line)


all_rows = [i for i in range(0, 128)]
# print(len(all_rows))
# print(all_rows[27:49])
print(all_rows[-1])

for boarding in list:
    max = 128
    min = 0
    # print(boarding)
    for i, row in enumerate(boarding):
        if row == "F":
            max = all_rows[int(len(all_rows)/2) - 1]
            all_rows = all_rows[0:max]
        elif row == "B":
            min = all_rows[int(len(all_rows)/2) - 1]
            # all_rows = all_rows[min:-1]
        elif i == 7:
            continue
    print(min, max, all_rows[min:max])

