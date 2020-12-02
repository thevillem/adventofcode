def main():
    password_list = []
    with open("day2_input.txt") as f:
        for line in f.readlines():
            password_list.append(line.strip())


    for password in password_list:
        result = password.split(' ')
        policy = result[0].split('-')
        character = result[1][0]
        
        char_count = result[2].count(character)
        if int(policy[0]) <= char_count <= int(policy[1]):
            pass
        

    valid = 0
    for password in password_list:
        result = password.split(' ')
        policy = result[0].split('-')
        character = result[1][0]

        if character in result[2]:
            if character == result[2][int(policy[0]) - 1] and character != result[2][int(policy[1]) - 1]:
                valid += 1
            elif character != result[2][int(policy[0]) - 1] and character == result[2][int(policy[1]) - 1]:
                valid += 1
            
    print(valid)

if __name__ == "__main__":
    main()