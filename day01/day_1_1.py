
depth_measurements = []
with open('input.txt') as file:
    lines = file.read().splitlines()
    for line in lines:
        depth_measurements.append(int(line))

previous = None
differences = []
increased_count = 0
for measurement in depth_measurements:
    if (previous == None):
        previous = 0
        current = measurement
    else:
        previous = current
        current = measurement
        difference = current - previous
        if (difference > 0): increased_count += 1
        differences.append(difference)

print(increased_count)
