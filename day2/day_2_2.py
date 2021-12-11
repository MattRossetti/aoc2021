commands = []
with open('input.txt') as file:
    lines = file.read().splitlines()
    for line in lines:
        commands.append(line)

commands_seperated = []
for command in commands:
    commands_seperated.append(command.split())

horizontal_pos = 0
aim = 0
depth = 0

for command in commands_seperated:
    if command[0] == 'down': aim += int(command[1])
    if command[0] == 'up': aim -= int(command[1])
    if command[0] == 'forward':
        horizontal_pos += int(command[1])
        depth += aim * int(command[1])

print(horizontal_pos * depth)