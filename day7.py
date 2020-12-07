import re


contains = {}
for line in open("day7_input.txt","r"):
    m = re.split(" bags contain ", line.strip())
    bags = m[1].replace(" bags", '').replace(".", '').replace(" bag", '').replace('no other', '0 other'). split(', ')
    pairs = [bag.split(' ', maxsplit=1) for bag in bags]
    contains[m[0]] = [(int(child[0]), child[1]) for child in pairs]

def find_parents(child):
    parents = set()
    [parents.add(k) for k,v in contains.items() if child in [color for number, color in v]]
    parents.discard(child) # prevent infinite recursion
    return parents

def get_roots(color, tree):
    parents = find_parents(color)
    if parents:
        tree |= parents
        for p in parents:
            get_roots(p, tree)
    return tree

def count_children(color):
    return 1 + sum(
        int(quantity) * count_children(color)
        for quantity, color in contains[color]
        if color != 'other'
    )

def main():

    ancestry = get_roots("shiny gold", set())
    print(f"Puzzle 1: {len(ancestry)}")

    print(f"Puzzle 2: {count_children('shiny gold')-1}")

if __name__ == "__main__":
    main()