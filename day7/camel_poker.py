"""
Main structure for this puzzle is going to be:
dict(hand_ID)
every hand_ID is associated with a dict with values:
(hand, bid, hand_type, order_number)
First all the hand_types need to be determined,
After wards they need to be sorted within the hand_types to an order
within that hand_type. Starting at the strongest hand type, which gets the
highest order_number and so forth.

Maybe keep another dict with all the hand_types and associated hand_IDs?
"""


def determine_hand_type(hand):
    hand_type = 'high_card'

    return hand_type


hand_types = ['high_card', 'one_pair', 'two_pair', 'three_kind',
              'full_house', 'four_kind', 'five_kind']

i = 0
card_dict = dict()
type_dict = dict()
for hand_type in hand_types:
    type_dict[hand_type] = []

with open("day7/test_input.txt", 'r') as f:
    line = f.readline()
    # stops if EOF
    while line != '':
        i += 1
        # strips because ofc
        line = line.strip()
        card_dict[i] = dict(hand=line.split()[0],
                            bid=line.split()[1])
        hand_type = determine_hand_type(line.split()[0])
        type_dict[hand_type].append(i)

        # reads next line to update while loop condition
        line = f.readline()

print(card_dict)
