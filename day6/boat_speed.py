with open('day6/test_input.txt', 'r') as f:
    times = f.readline()
    dist = f.readline()

times = times.split(':')[1].split()
dist = dist.split(':')[1].split()

time_dist = dict()
for i, time in enumerate(times):
    time_dist[int(time)] = int(dist[i])


# now need to determine how long to PRESS THE GAS!
# start in the middle, then work to the lowest time and highest time to press the gas and win
