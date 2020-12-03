def count_trees_w_slope(input, right, down):
    sled_position = 0
    trees = 0
    for line in input.split('\n')[0::down]:
        if line[sled_position] == '#':
            trees += 1
        sled_position = (sled_position + right) % len(line)
        print(sled_position)
    return trees

def main():
    with open("day3_input.txt") as f:
        terrain = f.read()

    slope_1 = count_trees_w_slope(terrain, 1, 1)
    puzzle_1 = count_trees_w_slope(terrain, 3, 1)
    slope_2 = count_trees_w_slope(terrain, 5, 1)
    slope_3 = count_trees_w_slope(terrain, 7, 1)
    slope_4 = count_trees_w_slope(terrain, 1, 2)
    
    print(f"Puzzle 1: {puzzle_1}")
    puzzle_2 = slope_1 * puzzle_1 * slope_2 * slope_3 * slope_4
    print(f"Puzzle 2: {puzzle_2}")

   

if __name__ == "__main__":
    main()