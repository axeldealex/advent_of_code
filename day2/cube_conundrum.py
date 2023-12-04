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

# setting the max amount of cubes allowed to be grabbed
max_red = 12
max_green = 13
max_blue = 14

# inits list that will keep track of game IDs
# first is False for easier counting later
possible = [False]
# sets an index for counting the game number
i = 0
# loops over all games
for game in input_text:
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
            if col == 'red' and num > max_red:
                possible[i] = False
            elif col == 'green' and num > max_green:
                possible[i] = False
            elif col == 'blue' and num > max_blue:
                possible[i] = False

print(possible)
id_sum = 0
for i, s in enumerate(possible):
    if s:
        id_sum += i

print(id_sum)
