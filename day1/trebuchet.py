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

cal_num = 0
# goes over all the input strings
for inputs in input_calibration:
    for i, s in enumerate(inputs):
        # checks if s is a digit
        if s.isdigit():
            # and saves if so, breaks for
            first_num = s
            break

    # same story here
    for i, s in enumerate(inputs[::-1]):
        if s.isdigit():
            second_num = s
            break
    temp = first_num + second_num  # don't worry about this soft error, it is not an error
    cal_num += int(temp)

print(cal_num)
