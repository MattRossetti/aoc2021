lantern_fish_list = []

class LanternFish:
    def __init__(self, timer):
        self.timer = timer
    def decrement(self):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            return True
        return False

with open ('example.txt') as file:
    input = file.readline().split(',')
    for fish in input:
        lantern_fish_list.append(LanternFish(int(fish)))

# for fish in lantern_fish_list:
#     print(fish.timer)

day = 1
stop_day = 256
while day < stop_day + 1:
    child_fish_list = []
    for fish in lantern_fish_list:
        new_fish = fish.decrement()
        if new_fish:
            child_fish_list.append(LanternFish(8))
    for child_fish in child_fish_list:
        lantern_fish_list.append(child_fish)
    timers = []
    for fish in lantern_fish_list:
        timers.append(fish.timer)
    # print('day', day, timers)
    print(day)
    day += 1

print(len(lantern_fish_list))