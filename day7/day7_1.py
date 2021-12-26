numbers = []
with open('input.txt') as f:
    input = f.readline().split(',')
    for number in input:
        numbers.append(int(number))

sorted_set = set(sorted(numbers))

set_min = min(sorted_set)
set_max = max(sorted_set)


distances = []
for set_number in sorted_set:
    distance = 0
    for number in numbers:
        distance += abs(set_number - number)
    distances.append((set_number, distance))

print(distances)

min_distance = (None, None)
for distance in distances:
    if min_distance[1] == None or distance[1] < min_distance[1]:
        min_distance = distance

print(min_distance)

