import sys

list = []

for line in sys.stdin:
    list.append(line)


boarding_passes = []

for i in range(len(list)):
    all_rows = [i for i in range(0, 128)]
    all_columns = [i for i in range(0, 8)]

    for row in list[i]:
        if row == "F":
            all_rows = all_rows[:len(all_rows)//2]
        elif row == "B":
            all_rows = all_rows[len(all_rows)//2:]
        elif row == "L":
            all_columns = all_columns[:len(all_columns)//2]
        elif row == "R":
            all_columns = all_columns[len(all_columns)//2:]

    row = all_rows[0]
    column = all_columns[0]
    seat_id = (row*8) + column
    boarding_passes.append(seat_id)


# -------------- Part 2 ----------------

boarding_passes = sorted(boarding_passes)
# print(sorted(boarding_passes))

for i in range(1, len(boarding_passes)):
    if boarding_passes[i] - boarding_passes[i-1] != 1:
        print(boarding_passes[i]-1)

