with open("day5/final_input.txt", 'r') as f:
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

# first extract the seed numbers
seeds = concat_file.pop(0).split(':')[1].strip().split()

map_dict = dict()
# then do the mapping
for line in concat_file:
    # new mapping - create a new entry in the mapping dict and retains key of this dict
    if 'map' in line:
        map_dict[line.split()[0]] = dict()
        cur_dict = line.split()[0]
    # saves the specific range
    else:
        nums = line.split()
        mapped_range = tuple([int(nums[0]), int(nums[0]) + int(nums[2]) - 1])
        map_range = tuple([int(nums[1]), int(nums[1]) + int(nums[2]) - 1])
        map_dict[cur_dict][map_range] = mapped_range   # PyCharm HATES having variables that could be undefined :^)

# print(seeds)
lowest_loc = -1
# go through all the seeds
#TODO
# to make this work for part 2, you need to track ranges of seeds and split them
# if their paths diverge. That is an insane exercise in bookkeeping that I frankly,
# do not care for to do rn.

for seed in seeds:
    seed = int(seed)
    # and for all the mappings
    for mapping in map_dict.keys():
        # we now have the seed number and the key of the first dict we need to check it against
        # go through the keys of the dict in the dict, see if we're inside the range
        # if not, we take the same number and continue with the next mapping
        ranges = map_dict[mapping].keys()
        # print(f'For mapping {mapping} we have seed {seed}')

        # goes through all the source ranges inside the mapping
        for map_range in ranges:

            # if we're inside one of the ranges, update our number and continue to the next mapping
            # if not we keep seed the same number and go to the next mapping
            if map_range[1] >= seed >= map_range[0]:
                # print(f'{seed} is between {map_range[1]} and {map_range[0]}')
                destination_min = map_dict[mapping][map_range][0]
                seed = destination_min + (seed - map_range[0])
                # print(f'new number is: {seed}')
                break
    if mapping == list(map_dict.keys())[-1] and lowest_loc == -1:
        lowest_loc = seed
    elif seed < lowest_loc:
        lowest_loc = seed

print(lowest_loc)
