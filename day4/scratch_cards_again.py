# THIS IS SUPER BAD CODE - COPIES CAN BE MULTIPLIED INSTEAD OF CALCULATED AGAIN EVERY TIME
# copies = get_hits(line)

def get_hits(scratch_card):
    your_numbers, winning_numbers = extract_numbers(scratch_card=scratch_card)
    hits = 0

    for number in your_numbers:
        if number in winning_numbers:
            hits += 1
    copies_inner = [1] * hits
    return copies_inner


def extract_numbers(scratch_card):
    numbers = scratch_card.split(':')[1].strip().split('|')
    your_numbers = numbers[0].strip().split()
    winning_numbers = numbers[1].strip().split()

    return your_numbers, winning_numbers


with open("day4/final_input.txt", 'r') as f:
    line = f.readline()
    temp, _ = extract_numbers(line)
    runs_outer = [1] * len(temp)
    cards = 0
    card_id = 1
    # stops if EOF
    while line != '':
        # strips because ofc
        line = line.strip()
        # determines how often we need to analyse a card
        runs_outer.append(1)
        runs = runs_outer.pop(0)

        # runs over the card a certain amount of times, adding 1 to the count each time
        for i in range(runs):
            cards += 1
            copies = get_hits(line)
            runs_outer[0:len(copies)] = [x + y for x, y in zip(runs_outer, copies)]
        # reads next line to update while loop condition
        # print(f'After card {card_id} we have counted a total of {cards} cards')
        card_id += 1
        line = f.readline()

print(cards)
