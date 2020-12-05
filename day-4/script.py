import sys

valid_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

correct = 0
text = ""
passports = []


for line in sys.stdin.readlines():
    text = text + " " + line

list = text.split(" \n")

for entry in list:
    fields = entry.replace("\n", "").strip().rstrip().split(" ")
    new_dict = {}

    for field in fields:
        key = field.split(":")[0]
        value = field.split(":")[1]
        new_dict[key] = value

    passports.append(new_dict)


# for passport in passports:
#     if all(valid in passport.keys() for valid in valid_fields):
#         correct += 1

valid_rules = [
    {
        "name": "byr",
        "length": 4,
        "min": 1920,
        "max": 2002

    },
    {
        "name": "iyr",
        "length": 4,
        "min": 2010,
        "max": 2020

    },
    {
        "name": "eyr",
        "length": 4,
        "min": 2020,
        "max": 2030

    },
    {
        "name": "hgt",
        "in": {
            "min": 59,
            "max": 76
        },
        "cm": {
            "min": 150,
            "max": 193
        }

    },
    {
        "name": "hcl",
        "first": "#",
        "length": 6,
        "number": {
            "min": 0,
            "max": 9
        },
        "letter": {
            "min": "a",
            "max": "f"
        }


    },
    {
        "name": "ecl",
        "color": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    },
    {
        "name": "pid",
        "first": 0,
        "length": 9,

    },
]


def val_byr(dict):


def validation(dict):


    # -------------------- Part 2 --------------------
for passport in passports:
