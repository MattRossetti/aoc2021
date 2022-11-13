def replace_at_index(str, index, new_char):
    new_str = ""
    for i, char in enumerate(str):
        if i != index:
            new_str += char
            continue
        new_str += new_char
    return new_str

def draw_map(target_x, target_y):
    map = ["." * (target_x[1] + 1) for _ in range(abs(target_y[0]) + 1)]
    map[0] = replace_at_index(map[0], 0, "S")
    for y in range(abs(target_y[1]), abs(target_y[0]) + 1):
        for x in range(target_x[0], target_x[1] + 1):
            map[y] = replace_at_index(map[y], x, "T")
    return map


def mark_step(map, initial_loc, step_x, step_y):
    if step_x >= len(map[0]): return map
    if step_y >= len(map): return map
    new_y = initial_loc[1] + abs(step_y)
    new_x = initial_loc[0] + step_x
    map[abs(step_y)] = replace_at_index(map[new_y], new_x, "#")     
    return map


def update_velocity(velocity, count):
    if velocity[0] > 0: velocity[0] = velocity[0] - 1
    velocity[1] = velocity[1] - (count + 1)
    return velocity


def check_overshoot(current_location, map):
    if current_location[0] >= len(map[0]): return True
    if current_location[1] >= len(map): return True
    return False


# example input
target_x = [20, 30]
target_y = [-10, -5]
# initial_vel = [9, 0]
initial_vel = [6, 3]
initial_loc = [0, 0]

map = draw_map(target_x, target_y)

overshot = False
velocity = initial_vel
location = initial_loc
count = 0
while overshot == False:
    print("location: ", location)
    print("velocity: ", velocity)
    map = mark_step(map, location, velocity[0], velocity[1])
    location[0] += velocity[0]
    location[1] += velocity[1]
    velocity = update_velocity(velocity, count)
    next_loc = [location[0], location[1]]
    next_loc[0] += velocity[0]
    next_loc[1] += velocity[1]
    overshot = check_overshoot(next_loc, map)
    count += 1
    print("check location: ", (location[1] * -1))
    if count == 5: break
    

print()
for line in map: print(line)
