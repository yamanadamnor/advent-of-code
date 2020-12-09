import sys
import itertools
lista = []
wrong = 0

for line in sys.stdin:
    lista.append(int(line))


def check_me(number, index):
    correct = False

    for num2 in lista[index-25:index]:

        if any(num2+num3 == number for num3 in lista[index-25:index]):
            correct = True

    return correct


# for i, num in enumerate(lista):
#     sum = 0
#     # print(len(lista[i-5: i]))

#     if i >= 25:
#         # print(check_me(num, i))
#         if check_me(num, i) is False:
#             wrong = num

# --------------- Part 2 ---------------
target = wrong

for n in range(2, len(lista)):
    for i in range(len(lista)):
        comb = lista[i:i+n]
        if sum(comb) == target:
            print(min(comb) + max(comb))

