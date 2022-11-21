import ast


class SnailFish:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

    def __str__(self):
        if isinstance(self.value, int):
            return str(self.value)
        return f"[{str(self.left)}, {str(self.right)}]"


def parse(snail_fish_num):
    root = SnailFish()
    if isinstance(snail_fish_num, int):
        root.value = snail_fish_num
        return root
    root.left = parse(snail_fish_num[0])
    root.right = parse(snail_fish_num[1])
    root.left.parent = root
    root.right.parent = root
    return root


def check_if_in_snail_fish(snail_fish, new_snail_fish):
    if isinstance(snail_fish.value, int):
        return False
    if snail_fish == new_snail_fish:
        return True
    if check_if_in_snail_fish(snail_fish.left, new_snail_fish) == True:
        return True
    if check_if_in_snail_fish(snail_fish.right, new_snail_fish) == True:
        return True
    return False


def explode(snail_fish, left_value=None, right_value=None, new_snail_fish=None):
    if not check_if_in_snail_fish(snail_fish.left, new_snail_fish) and new_snail_fish is not None and left_value is not None:
        if isinstance(snail_fish.left.right, SnailFish):
            if isinstance(snail_fish.left.right.right, SnailFish):
                if isinstance(snail_fish.left.right.right.right, SnailFish):
                    if isinstance(snail_fish.left.right.right.right.right, SnailFish):
                        snail_fish.left.right.right.right.right.value += left_value
                        left_value = None
                    else:
                        snail_fish.left.right.right.right.value += left_value
                        left_value = None
                else:
                    snail_fish.left.right.right.value += left_value
                    left_value = None
            else:
                snail_fish.left.right.value += left_value
                left_value = None

    if not check_if_in_snail_fish(snail_fish.right, new_snail_fish) and new_snail_fish is not None and right_value is not None:
        if isinstance(snail_fish.right.left, SnailFish):
            if isinstance(snail_fish.right.left.left, SnailFish):
                if isinstance(snail_fish.right.left.left.left, SnailFish):
                    if isinstance(snail_fish.right.left.left.left.left, SnailFish):
                        snail_fish.right.left.left.left.left.value += right_value
                        right_value = None
                    else:
                        snail_fish.right.left.left.left.value += right_value
                        right_value = None
                else:
                    snail_fish.right.left.left.value += right_value
                    right_value = None
            else:
                snail_fish.right.left.value += right_value
                right_value = None

    # if not check_if_in_snail_fish(snail_fish.right, new_snail_fish) and new_snail_fish is not None and right_value is not None:
    #     if isinstance(snail_fish.right.left, SnailFish):
    #         if isinstance(snail_fish.right.left.left, SnailFish):
    #             if isinstance(snail_fish.right.left.left.left, SnailFish):
    #                 print(snail_fish.right.left.left.left.value)
    #                 snail_fish.right.left.left.left.value += right_value
    #                 right_value = None
    #     if isinstance(snail_fish.right.left, SnailFish) and right_value is not None:
    #         if isinstance(snail_fish.right.left.left, SnailFish):
    #             snail_fish.right.left.left.value += right_value
    #             right_value = None
    #         else:
    #             snail_fish.right.left.value += right_value
    #             right_value = None

    # if not check_if_in_snail_fish(snail_fish.left, new_snail_fish) and new_snail_fish is not None and left_value is not None:
    #     if snail_fish.left.right is not None:
    #         # if snail_fish.left.right.value is not None:
    #         snail_fish.left.right.value += left_value
    #         left_value = None

    # if not check_if_in_snail_fish(snail_fish.right, new_snail_fish) and new_snail_fish is not None and right_value is not None:
    #     if snail_fish.right.left is not None:
    #         # if snail_fish.right.left.value is not None:
    #         snail_fish.right.left.value += right_value
    #         right_value = None

    if snail_fish.parent is None:
        return snail_fish

    if left_value is not None and snail_fish.left.value is not None:
        snail_fish.left.value += left_value
        left_value = None

    if right_value is not None and snail_fish.right.value is not None:
        snail_fish.right.value += right_value
        right_value = None

    if snail_fish.left.value is None and left_value is None and right_value is None and new_snail_fish is None:
        # print("ex left")
        left_value = snail_fish.left.left.value
        if snail_fish.right.value is None:
            snail_fish.right.left.value += snail_fish.left.right.value
        else:
            snail_fish.right.value += snail_fish.left.right.value
        snail_fish.left = SnailFish(0)
        snail_fish.left.parent = snail_fish
        right_value = None
        new_snail_fish = snail_fish

    if snail_fish.right.value is None and left_value is None and right_value is None and new_snail_fish is None:
        # print("ex right")
        right_value = snail_fish.right.right.value
        snail_fish.left.value += snail_fish.right.left.value
        left_value = None
        snail_fish.right = SnailFish(0)
        snail_fish.right.parent = snail_fish
        new_snail_fish = snail_fish

    return explode(snail_fish.parent, left_value, right_value, new_snail_fish)


def find_explode(snail_fish, depth=0, exploded=False):
    if isinstance(snail_fish.value, int):
        return snail_fish, exploded
    if depth == 4 and exploded is False:
        snail_fish = explode(snail_fish.parent)
        exploded = True
        return snail_fish, exploded
    tmp, exploded = find_explode(snail_fish.left, depth + 1, exploded)
    tmp, exploded = find_explode(snail_fish.right, depth + 1, exploded)
    return snail_fish, exploded


def split(snail_fish, splited=False):
    if isinstance(snail_fish.value, int):
        if snail_fish.value >= 10 and splited is False:
            tmp_val = snail_fish.value
            remainder = tmp_val % 2
            left_val = tmp_val // 2
            right_val = tmp_val // 2 + remainder
            snail_fish.value = None
            snail_fish.left = SnailFish(left_val)
            snail_fish.left.parent = snail_fish
            snail_fish.right = SnailFish(right_val)
            snail_fish.right.parent = snail_fish
            splited = True
        return snail_fish, splited
    tmp, splited = split(snail_fish.left, splited)
    tmp, splited = split(snail_fish.right, splited)
    return snail_fish, splited


# def find_and_action(snail_fish, depth=0, exploded=False, splited=False):
#     if not isinstance(snail_fish.value, int) and depth > 3 and exploded is False and splited is False:
#         if (snail_fish.left.value < 10 and snail_fish.right.value < 10) or (isinstance(snail_fish.left, SnailFish) or isinstance(snail_fish.right, SnailFish)):
#             print("exploding: ", snail_fish)
#             print("exploding parent: ", snail_fish.parent)
#             snail_fish = explode(snail_fish.parent)
#             exploded = True
#             return snail_fish, exploded, splited
#     if isinstance(snail_fish.value, int):
#         if snail_fish.value >= 10 and exploded is False and splited is False:
#             print("spliting", snail_fish)
#             tmp_val = snail_fish.value
#             remainder = tmp_val % 2
#             left_val = tmp_val // 2
#             right_val = tmp_val // 2 + remainder
#             snail_fish.value = None
#             snail_fish.left = SnailFish(left_val)
#             snail_fish.left.parent = snail_fish
#             snail_fish.right = SnailFish(right_val)
#             snail_fish.right.parent = snail_fish
#             splited = True
#         return snail_fish, exploded, splited
#     tmp, exploded, splited = find_and_action(
#         snail_fish.left, depth + 1, exploded, splited)
#     tmp, exploded, splited = find_and_action(
#         snail_fish.right, depth + 1, exploded, splited)
#     return snail_fish, exploded, splited


# def reduce(snail_fish, exploded=True, splited=True):
#     while exploded is True or splited is True:
#         print(snail_fish)
#         snail_fish, exploded, splited = find_and_action(snail_fish)
#         if exploded:
#             print("exploded")
#         if splited:
#             print("splited")
#     return snail_fish


def reduce(snail_fish, exploded=True, splited=True):
    while exploded is True or splited is True:
        print(snail_fish)
        snail_fish, exploded = find_explode(snail_fish)
        if exploded:
            print("exploded")
            continue
        snail_fish, splited = split(snail_fish)
        if splited:
            print("splited")
    return snail_fish


def add_and_reduce(snail_fish, next_snail_fish):
    new_snail_fish = SnailFish()
    snail_fish.parent = new_snail_fish
    new_snail_fish.left = snail_fish
    next_snail_fish.parent = new_snail_fish
    new_snail_fish.right = next_snail_fish
    new_snail_fish = reduce(new_snail_fish)
    return new_snail_fish


def input_to_list(input_file):
    fish_num = []
    with open(input_file) as file:
        lines = file.read().splitlines()
        for line in lines:
            line = ast.literal_eval(line)
            fish_num.append(line)
    return fish_num


def add(fish_num):
    snail_fish_0 = parse(fish_num[0])
    snail_fish_1 = parse(fish_num[1])
    snail_fish = add_and_reduce(snail_fish_0, snail_fish_1)
    count = 2
    while count < len(fish_num):
        next_snail_fish = parse(fish_num[count])
        snail_fish = add_and_reduce(snail_fish, next_snail_fish)
        count += 1
    return snail_fish


def find_magnitude(snail_fish):
    if snail_fish.left is not None:
        snail_fish.left = find_magnitude(snail_fish.left)
    if snail_fish.right is not None:
        snail_fish.right = find_magnitude(snail_fish.right)
    if isinstance(snail_fish.left, SnailFish) and isinstance(snail_fish.right, SnailFish):
        if isinstance(snail_fish.left.value, int) and isinstance(snail_fish.right.value, int):
            tmp_fish = snail_fish
            snail_fish = SnailFish(
                snail_fish.left.value * 3 + snail_fish.right.value * 2)
            snail_fish.parent = tmp_fish.parent
            return snail_fish
    return snail_fish


# snail_fish_num_1 = [1, 2]
# snail_fish_num_2 = [[1, 2], 3]
# snail_fish_num_3 = [[[[[9, 8], 1], 2], 3], 4]
# snail_fish_num_4 = [[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]]
# snail_fish_num_5 = [[[[0, 7], 4], [7, [[8, 4], 9]]], [1, 1]]
# snail_fish_num_6 = [[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]]
# snail_fish_num_7 = [[[[0, 7], 4], [15, [0, 13]]], [1, 1]]
# snail_fish_num_8 = [[[[[1, 1], [2, 2]], [3, 3]], [4, 4]], [5, 5]]
# snail_fish_num_9 = [[9, 1], [1, 9]]
# snail_fish_num_10 = [[1, 2], [[3, 4], 5]]
# snail_fish_num_11 = [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]],
#                      [[[0, 7], [6, 6]], [8, 7]]]
#
#
# snail_fish = parse(snail_fish_num_11)
# print(snail_fish)
# snail_fish = find_magnitude(snail_fish)
# print(snail_fish)


# snail_fish = parse(snail_fish_num_5)
# print(snail_fish)
# snail_fish, exploded, splited = find_and_action(snail_fish)
# print(snail_fish, "ex", exploded, "sp", splited)

# snail_fish = parse(snail_fish_num_4)
# print(snail_fish)
# snail_fish = reduce(snail_fish)
# print(snail_fish)

# snail_fish, exploded = find_explode(snail_fish)
# print(snail_fish)
# snail_fish, splited = split(snail_fish)
# print(snail_fish, splited)

fish_num = input_to_list("input_example_18.txt")
print(fish_num)
print()
snail_fish = add(fish_num)
print("reduced_snail_fish: ", snail_fish)
magnitude = find_magnitude(snail_fish)
print("ANSWER IS")
print("\t", magnitude)
