def update_location(location, velocity):
    location[0] += velocity[0]
    location[1] += velocity[1]
    return location


def update_velocity(velocity):
    if velocity[0] > 0:
        velocity[0] = velocity[0] - 1
    velocity[1] = velocity[1] - 1
    return velocity


def check_in_target(location, target_x, target_y):
    if location[0] < target_x[0]: return False
    if location[0] > target_x[1]: return False
    if location[1] > target_y[0]: return False
    if location[1] < target_y[1]: return False
    return True


def check_overshoot(location, target_x, target_y):
    if location[0] > target_x[1] + 1: return True
    if location[1] < target_y[1] - 1: return True
    return False


def find_hit(target_x, target_y, initial_loc, initial_vel):
    loc = initial_loc.copy()
    vel = initial_vel.copy()
    overshot = False
    in_target = False
    while in_target == False and overshot == False:
        loc = update_location(loc, vel)
        # print(loc)
        vel = update_velocity(vel)
        in_target = check_in_target(loc, target_x, target_y)
        overshot = check_overshoot(loc, target_x, target_y)
    if in_target == True:
        print("hit! vel set to: ", initial_vel)
        return (initial_vel[0], initial_vel[1])
    return None


# example inputs
# target_x = [20, 30]
# target_y = [-5, -10]
# initial_loc = [0, 0]
# initial_vel = [7, 2]
# initial_vel = [6, 3]
# initial_vel = [9, 0]
# initial_vel = [17, -4]
# initial_vel = [6, 9]

# part 1 inputs
target_x = [102, 157]
target_y = [-90, -146]
initial_loc = [0,0]



# print(find_hit(target_x, target_y, initial_loc, [16, -4]))
# quit()



hits = set()
for vx in range(target_x[1] + 1):
    for vy in range(target_y[1], abs(target_y[1])):
        # print([vx, vy])
        hit = find_hit(target_x, target_y, initial_loc, [vx, vy])
        # print(height)
        if hit == None: continue
        hits.add(hit)

print("total hits: ", len(hits))

