input_text = []
# start by parsing a single line
with open("day3/test_input.txt", 'r') as f:
    line = f.readline()
    # stops if EOF
    while line != '':
        # strips because ofc
        line = line.strip()
        input_text.append(line)
        # reads next line to update while loop condition
        line = f.readline()

# loop over the input to identify special characters and numbers
for line in input_text:
    pass
