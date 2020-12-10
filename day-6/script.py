import sys

list = []
list2 = []
temp_list = []

for line in sys.stdin:
    list.append(line)

for i, answer in enumerate(list):
    if answer == "\n" or i == len(list):
        list2.append(temp_list)
        temp_list = []
    else:
        temp_list.append(answer.strip())

for i, answer in list2:


