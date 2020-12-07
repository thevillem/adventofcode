
def main():
    inputList = [int(line.translate("".maketrans('FBLR', '0101')), 2) for line in open('day5_input.txt')]

    print(inputList)

    # Part I
    print(f'Highest seat-id: {max(inputList)}')

    # Part II
    print(f'Missing seat-id: {set(range(min(inputList), max(inputList))) - set(inputList)}')       

if __name__ == "__main__":
    main()