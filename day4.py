from collections import Counter
import re

def ishex(text: str, search=re.compile(r'[^a-f0-9.]').search):
    return not bool(search(text))

def isnum(text: str, search=re.compile(r'[^0-9.]').search):
    return not bool(search(text))

def parse_passports(documents):
    needed_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid = 0
    for _, value in documents.items():
        fields = [field.split(":")[0] for field in value]
        values = [field.split(":")[1] for field in value]
        document = dict(zip(fields, values))
        diff = list(Counter(needed_fields) - Counter(fields))
        if not diff:
            check = 0
            # check the length of the years, ensuring 4 digits
            if len(document['byr']) == len(document['iyr']) == len(document['eyr']) == 4:
            
                if (1920 <= int(document['byr']) <= 2002):
                    check += 1

                if (2010 <= int(document['iyr']) <= 2020):
                    check += 1

                if (2020 <= int(document['eyr']) <= 2030):
                    check += 1

            if document["hgt"][-2:] == "cm" and 150 <= int(document["hgt"][:-2]) <= 193:
                check += 1

            elif document["hgt"][-2:] == "in" and 59 <= int(document["hgt"][:-2]) <= 76:
                check += 1

            if document["hcl"][0] == "#" and len(document["hcl"][1:]) == 6 and ishex(document["hcl"][1:]):
                check += 1

            if document["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                check += 1

            if isnum(document["pid"]) and len(document["pid"]) == 9:
                check += 1
            
            if check == 7:
                valid += 1
            
    print(valid)

def main():
    documents = {}
    with open("day4_input.txt") as f:
        passport = []
        i = 0
        for line in f.readlines():
            if line == "\n":
                i += 1
                passport = []
            else:
                if not passport:
                    passport = line.strip("\n").split(' ')
                else:
                    passport += line.strip("\n").split(' ')
            documents[i] = passport

    parse_passports(documents)

if __name__ == "__main__":
    main()