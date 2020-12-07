
def part1(input_path: str):
    return sum(
        len(set("".join(line.split('\n'))))
        for line in open(input_path).read().split("\n\n")
    )

def part2(input_path: str):          
        
    counts = 0
    for group in open(input_path).read().split("\n\n"):
        group_lst = group.split()
        group_count = set(group_lst[0])
        for person_answers in group_lst[1:]:
            group_count = group_count.intersection(person_answers)
        counts += len(group_count)
    
    return counts

def main():

    # part1_ans = part1("day6_input.txt")
        
    # print(f"Puzzle 1: {part1_ans}")

    part2_ans = part2("day6_input.txt")

    print(f"Puzzle 2: {part2_ans}")

if __name__ == "__main__":
    main()