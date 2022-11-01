def summation(start, end):
    difference = abs(end - start)
    summation = (difference * (difference + 1)) / 2
    return round(summation)

numbers = []
with open('input.txt') as f:
    input = f.readline().split(',')
    for number in input:
        numbers.append(int(number))

numbers_min = min(numbers)
numbers_max = max(numbers)

sorted_list = []
for i in range(numbers_min, numbers_max):
    sorted_list.append(i)

distances = []
for list_number in sorted_list:
    distance = 0
    for number in numbers:
        distance += summation(list_number, number)
    distances.append((list_number, distance))

print(distances)

min_distance = (None, None)
for distance in distances:
    if min_distance[1] == None or distance[1] < min_distance[1]:
        min_distance = distance

print(min_distance)

