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


def extract_features(line, num_dict, symbol_dict, row_num, flag=0, flag_while=0):
    """
    Function for extracting the location of numbers and symbols in the input.
    Outputs of this function are later used for valid_check, which checks whether a number should be included.
    """
    for i, s in enumerate(line):
        row_length = len(line) - 1
        # skips over dots/empty sections
        if flag:
            flag -= 1
            continue
        if s == '.':
            continue
        # extracts numbers first
        elif s.isdigit():
            min_index = i
            max_index = i
            # time to do a disgusting bodge to see how long the number is
            j = i

            while line[j+1].isdigit():
                flag += 1
                j += 1
                max_index = j
                if j >= row_length:
                    break
            num_dict[row_num].append([min_index, max_index])
        # special character otherwise
        elif s == '*':
            # updates the list for that row entry with new index
            symbol_dict[row_num].append(i)

    return num_dict, symbol_dict


def gear_checking(num_dict, symbol_dict):
    counter = 0


    if counter == 2:
        return
    pass


# inits some empty dicts for location saving
num_dict = dict()
symbol_dict = dict()
# iteration to identify which line you're on
row_num = -1
# loop over the input to identify special characters and numbers
for line in input_text:
    # increments the row number
    row_num += 1
    # inits empty lists
    num_dict[row_num] = []
    symbol_dict[row_num] = []
    # extracts the location of numbers and symbols
    num_dict, symbol_dict = extract_features(line, num_dict, symbol_dict, row_num)

# calculates the final sum
final_sum = gear_checking(num_dict, symbol_dict)
print(final_sum)
