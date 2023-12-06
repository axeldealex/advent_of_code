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


def extract_features(line, num_dict, symbol_dict, row_num, flag=0,):
    """
    Function for extracting the location of numbers and symbols in the input.
    Outputs of this function are later used for gear_checking, which checks whether a number should be included.
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


def gear_checking(numbers, symbol_dict):
    num_sum = 0

    # unpacks the key (row_number) and value (index of *)
    for i, s in enumerate(symbol_dict.values()):
        upper = True
        lower = True
        # determines which rows need to be passed to check_number_presence
        min_row_idx = max(0, i-1)
        max_row_idx = min(len(numbers)-1, i+2)

        # gets conditions for first and last row, special cases for check_number_presence
        if max_row_idx - min_row_idx == 2:
            if min_row_idx == 0:
                upper = False
            else:
                lower = False

        # early exit for when there is no symbol in the row
        if not s:
            continue
        # goes over all stars in a row
        for idx in s:
            factor = check_number_presence(numbers[min_row_idx:max_row_idx], idx, upper, lower)
            num_sum += factor
    return num_sum


def check_number_presence(num_row, idx, upper, lower):
    counter = 0
    factor = 0
    if upper and lower:
        for i in range(idx-1, idx+2):
            num_row
        pass
    if counter == 2:
        return factor
    return 0

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
final_sum = gear_checking(input_text, symbol_dict)
print(final_sum)
