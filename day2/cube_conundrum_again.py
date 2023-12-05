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

            # checks every min_colour against the current value
            if col == 'red' and num > min_red:
                min_red = num
            elif col == 'green' and num > min_green:
                min_green = num
            elif col == 'blue' and num > min_blue:
                min_blue = num
    power_sum += min_red * min_green * min_blue

print(power_sum)
