
depth_measurements = []
with open('input.txt') as file:
    lines = file.read().splitlines()
    for line in lines:
        depth_measurements.append(int(line))

previous_window = None
differences = []
increased_count = 0
for i in range(len(depth_measurements)):
    if i + 2 > len(depth_measurements) - 1: break
    if previous_window == None:
        previous_window = 0
        current_window = depth_measurements[i] + depth_measurements[i + 1] + depth_measurements[i + 2]
    else:
        previous_window = current_window
        current_window = depth_measurements[i] + depth_measurements[i + 1] + depth_measurements[i + 2]
        # print(previous_window, current_window)
        difference = current_window - previous_window
        if difference > 0: increased_count += 1

print(increased_count)
