input_text = []
# start by parsing a single line
with open("day2/final_input.txt", 'r') as f:
    line = f.readline()
    # stops if EOF
    while line != '':
        # strips because ofc
        line = line.strip()
        input_text.append(line)
        # reads next line to update while loop condition
        line = f.readline()

# inits list that will keep track of game IDs
# first is False for easier counting later
possible = [False]
# sets an index for counting the game number
i = 0
power_sum = 0
# loops over all games
for game in input_text:
    min_red = 0
    min_blue = 0
    min_green = 0
    # increments index
    i += 1
    # sets the default value to True
    possible.append(True)

    # starts string splitting the game values
    blocks = game.split(': ')[1]
    grabs = blocks.split('; ')

    # every grab in the game
    for grab in grabs:
        colour = grab.split(',')
        # and every colour of block in a grab
        for block in colour:
            # strips for consistent reading
            num = int(block.strip().split(' ')[0])
            col = block.strip().split(' ')[1]

            # print(f'{num} of {col}')
            # checks every colour against the max allowed of that colour
            # if condition is met changes the value in 'possible' list to False
            if col == 'red' and num > min_red:
                min_red = num
            elif col == 'green' and num > min_green:
                min_green = num
            elif col == 'blue' and num > min_blue:
                min_blue = num
    print(f'red:{min_red}\ngreen:{min_green}\nblue:{min_blue}')
    power_sum += min_red * min_green * min_blue

print(power_sum)