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


def extract_features(line, num_dict, symbol_dict, row_num, flag=0):
    """"
    Function for extracting the location of numbers and symbols in the input.
    Outputs of this function are later used for valid_check, which checks whether a number should be included.
    """
    for i, s in enumerate(line):
        row_length = len(line) - 3
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

            num_dict[row_num].append([min_index, max_index])
        # special character otherwise
        else:
            # updates the list for that row entry with new index
            symbol_dict[row_num].append(i)

    return num_dict, symbol_dict


def number_checking(num_dict, symbol_dict):
    """"
    Checks whether a number should be included in the final value calculation.
    Returns the sum of all the numbers.
    """
    # inits the counting variable
    valid_sum = 0
    max_rows = len(num_dict.keys()) - 1
    # goes over all the rows
    for row in num_dict.keys():
        num_row = num_dict[row]
        for numbers in num_row:
            # if not the first row, checks row above
            if row > 0:
                if check_symbol_presence(symbol_dict[row - 1], numbers[0], numbers[1]):
                    print(int(input_text[row][numbers[0]:numbers[1] + 1]))
                    valid_sum += int(input_text[row][numbers[0]:numbers[1]+1])
                    continue
            # if not last row, checks row below
            if row < max_rows:
                if check_symbol_presence(symbol_dict[row + 1], numbers[0], numbers[1]):
                    print(int(input_text[row][numbers[0]:numbers[1] + 1]))
                    valid_sum += int(input_text[row][numbers[0]:numbers[1]+1])
                    continue
                pass
            # checks the same row
            else:
                if check_symbol_presence(symbol_dict[row], numbers[0], numbers[1]):
                    print(int(input_text[row][numbers[0]:numbers[1] + 1]))
                    valid_sum += int(input_text[row][numbers[0]:numbers[1] + 1])

                    continue

    return valid_sum


def check_symbol_presence(symbol_row, min_idx, max_idx):
    for symbol in symbol_row:
        if symbol <= (min_idx-1) or symbol >= (max_idx+1):
            return True
    return False

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
final_sum = number_checking(num_dict, symbol_dict)
print(final_sum)
