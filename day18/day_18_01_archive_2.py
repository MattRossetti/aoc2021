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


def parse(snail_fish):
    root = SnailFish()
    if isinstance(snail_fish, int):
        root.value = snail_fish
        return root

    root.left = parse(snail_fish[0])
    root.right = parse(snail_fish[1])
    root.left.parent = root
    root.right.parent = root
    return root


def find_and_return_root(snail_fish):
    if snail_fish.parent is None:
        return snail_fish
    find_and_return_root(snail_fish.parent)


def explode(snail_fish):
    print(snail_fish)
    if isinstance(snail_fish.value, int):
        print("bottom")
        return
    explode(snail_fish.left)
    explode(snail_fish.right)


snail_fish_1 = [1, 2]
snail_fish_2 = [[1, 2], 3]
snail_fish_3 = [[[[[9, 8], 1], 2], 3], 4]
snail_fish_4 = [[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]]
snail_fish_5 = [[[[0, 7], 4], [7, [[8, 4], 9]]], [1, 1]]
parsed = parse(snail_fish_3)
print(parsed)
parsed = explode(parsed)
print()
print(parsed)
