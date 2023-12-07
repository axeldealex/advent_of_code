import math

with open('day6/final_input_again.txt', 'r') as f:
    times = f.readline()
    dist = f.readline()

times = times.split(':')[1].split()
dist = dist.split(':')[1].split()

time_dist = dict()
for i, time in enumerate(times):
    time_dist[i] = [int(time), int(dist[i])]

print(time_dist)
product = 1
# goes over all the times
for entry in time_dist.keys():
    # starts finding the minimum gas time to win, max is symmetrical to the other side
    target = time_dist[entry][1]
    time = time_dist[entry][0]
    print(f'need to hit {target} in {time}')
    for i in range(1, math.ceil(time + 1)):
        distance = (time - i) * i
        if distance > target:
            print(f'got to {distance} compared to {target}')
            min_time = i
            max_time = time - i
            product *= (max_time - min_time + 1)
            break

print(product)
