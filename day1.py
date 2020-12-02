from itertools import combinations

def main():
    expense_report = []
    with open("day1_input.txt") as f:
        for line in f.readlines():
            expense_report.append(int(line.strip()))


    for item in combinations(expense_report, 3):
        if sum(item) == 2020:
            print(item[0] * item[1] * item[2])
        
        

if __name__ == "__main__":
    main()