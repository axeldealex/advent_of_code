# inits a list for storage of inputs
input_calibration = []

# opens and reads the file
with open("day1/final_input.txt", 'r') as f:
    line = f.readline()
    # stops if EOF
    while line != '':
        # strips because ofc
        line = line.strip()
        input_calibration.append(line)
        # reads next line to update while loop condition
        line = f.readline()


def find_numbers(X):
    """"
    Find the number according the advent of code day 1 second challenge
    """
    num_found = dict()
    search_terms = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    # loops over all the search terms
    for i, search in enumerate(search_terms):
        # finds the first
        index = X.find(search)
        num_found[index] = i+1
        # and last occurrence of the word, which are added by index in the word
        index = X.rfind(search)
        num_found[index] = i+1

    # finds the first normal number
    for i, s in enumerate(X):
        if s.isdigit():
            # and saves if so, breaks afterwards
            num_found[i] = s
            break
    # and last
    for i, s in enumerate(X[::-1]):
        if s.isdigit():
            # have to recalculate the index because we're going in reverse
            i = len(X) - 1 - i
            num_found[i] = s
            break

    # then we remove the -1 index, as it is invalid (try in case of edge cases where every number is in the word)
    dict_idx = list(num_found.keys())
    try:
        dict_idx.remove(-1)
    except:
        print('Edge case!')

    # we index in the num_found dict with the index, which returns the number at that location
    first_num = int(num_found[min(dict_idx)])
    second_num = int(num_found[max(dict_idx)])

    # and recompose the number by doing the first digit times 10
    return first_num * 10 + second_num


cal_num = 0
# goes over all the input strings
for inputs in input_calibration:
    num = find_numbers(inputs)
    cal_num += num

# prints the sum of all calibration numbers, congratulations!
print(cal_num)
