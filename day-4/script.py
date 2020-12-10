import sys
import re

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


def validation(dict):
    byr = ("byr" in dict and len(dict["byr"]) == 4
           and int(dict["byr"]) >= 1920 and int(dict["byr"]) <= 2002)

    iyr = ("iyr" in dict and len(dict["iyr"]) == 4
           and int(dict["iyr"]) >= 2010 and int(dict["iyr"]) <= 2020)

    eyr = ("eyr" in dict and len(dict["eyr"]) == 4
           and int(dict["eyr"]) >= 2020 and int(dict["eyr"]) <= 2030 )

    hgt = False

    if "hgt" in dict and re.match("(\d+)([a-z]+)", dict["hgt"]):

        hgt_str = re.split("(\d+)([a-z]+)", dict["hgt"])

        if (hgt_str[2] == "cm" and int(hgt_str[1]) >= 150
                and int(hgt_str[1]) <= 193):
            hgt = True

        elif (hgt_str[2] == "in" and int(hgt_str[1]) >= 59
              and int(hgt_str[1]) <= 76):
            hgt = True

    hcl = False

    if ("hcl" in dict and len(dict["hcl"]) == 7 and
            re.match("^#([a-fA-F0-9]+$)", dict["hcl"])):
        hcl = True
    ecl = ("ecl" in dict and dict["ecl"] in
           ["amb", "blu", "brn" ,"gry", "grn" ,"hzl", "oth"])

    pid = ("pid" in dict and len(dict["pid"]) == 9
           and re.match("(\d+)", dict["pid"]))



    # print(byr , iyr , eyr , hgt , hcl , ecl , pid)
    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        return True
    else:
        return False



    # -------------------- Part 2 --------------------
for passport in passports:
    if validation(passport):
        correct += 1
        print(passport)



print(correct)
