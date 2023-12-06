def get_points(scratch_card):
    your_numbers, winning_numbers = extract_numbers(scratch_card=scratch_card)
    points = 0.5

    for number in your_numbers:
        if number in winning_numbers:
            points *= 2
    return int(points)


def extract_numbers(scratch_card):
    numbers = scratch_card.split(':')[1].strip().split('|')
    your_numbers = numbers[0].strip().split()
    winning_numbers = numbers[1].strip().split()

    return your_numbers, winning_numbers


points_sum = 0
with open("day4/final_input.txt", 'r') as f:
    line = f.readline()
    # stops if EOF
    while line != '':
        # strips because ofc
        line = line.strip()
        points_sum += get_points(line)
        # reads next line to update while loop condition
        line = f.readline()

print(points_sum)
