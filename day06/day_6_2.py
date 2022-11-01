from collections import OrderedDict

fish_dict = OrderedDict()
for i in range(0, 9): fish_dict[i] = 0
print(fish_dict)
with open('input.txt') as file:
    input = file.readline().split(',')
    for fish in input:
        fish_dict[int(fish)] = fish_dict.get(int(fish), 0) + 1


days = 256
for i in range(days):
    temp_dict = OrderedDict()
    for i in range(0, 9): temp_dict[i] = 0
    for key in fish_dict:
        if key == 0:
            temp_dict[6] = fish_dict[key]
            temp_dict[8] = fish_dict[key]
        else:
            temp_dict[key - 1] = temp_dict.get(key - 1, 0) + fish_dict[key]
    fish_dict = temp_dict

print(fish_dict)

total_fish = 0
for key in fish_dict:
    total_fish += fish_dict[key]

print(total_fish)

