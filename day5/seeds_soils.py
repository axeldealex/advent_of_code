with open("day5/test_input.txt", 'r') as f:
    concat_file = []
    flag = 0
    line = f.readline()
    # stops if EOF
    while line != '' and flag != 2:
        # strips because ofc
        line = line.strip()

        # exits if we have two blank lines in a row
        if line == '':
            flag += 1
        else:
            concat_file.append(line)
            flag = 0

        # reads next line to update while loop condition
        line = f.readline()


# continue the script after mapping all the inputs
print(concat_file)

# need to find way to save all the mapping in 1 dict?
# or use another data structure, not sure. Maybe use regex to identify when we enter a new mapping and use the name
# of the mapping as a key to the variable so that it's completely resistant to adding new maps
