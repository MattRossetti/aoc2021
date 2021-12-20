import math

# def findFish(days, start):
#     return pow(2,((days - start - 1) // 7))
# start = 0
# days = 8

# print(findFish(days, start))


# works if each fish starts with a timer of 6
# def findFish(days):
#     return pow(2,((days - 1) // 7))

# for i in range(1, 25):
#     print('day', i, 'fish', findFish(i))

# total_days = 256
# new_fish_days = []
# for day in range(total_days // 7):
#     new_fish_days.append((day + 1) * 7)

# print(new_fish_days)

# def findFish(days,start):
#     return 1 + ((days + (7 - start - 1)) // 7)
# days = 256
# start = 1
# # for i in range (0, days + 1):
# #     print('day:', i, 'fish:', findFish(i, start))   

# print(findFish(days, start))

# def findFish(days, offset, initial):
#     return (initial + (days + (7 - offset)) // 7)

# # for i in range(0, 19):
# #     print('day:', i, 'fish:', findFish(i, 2, 1))

# def findFish(days, count):
#     # print(days)
#     if days < 0:
#         return count
#     count += days // 7
#     count += days // 9
#     return (findFish(days - 7, count))

days_max = 256
def findFish(days, count):
    # print(days)
    if days >= days_max:
        return count
    count += days // 7
    return (findFish(days + 7, count) + findFish(days + 9, count))


print(findFish(5, 1))
