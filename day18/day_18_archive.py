# knowns
# if pair is nested inside four pairs -> leftmost pair exploes
# if number is 10 or greater -> leftmost regular number splits

def explode(snail_num, depth=0, exploded=False):
    new_num = []
    for num in snail_num:
        if type(num) != list:
            new_num.append(num) 
            continue
        next_num, exploded = explode(num, depth + 1, exploded)
        new_num.append(next_num)
    need_to_explode = False
    if depth == 3 and exploded == False:
        for num in snail_num:
            if type(num) == list:
                need_to_explode = True

    if need_to_explode == False: return new_num, exploded

    exploded_num = []
    if type(snail_num[0]) == list:
        exploded_num.append(0)
        exploded_num.append(snail_num[0][1] + snail_num[1])
    if type(snail_num[1]) == list:
        exploded_num.append(snail_num[0] + snail_num[1][0])
        exploded_num.append(0)
    return exploded_num, True


def split_num(snail_num, split=False):
    new_num = []
    if type(snail_num) == list:
         for num in snail_num:
             next_num, split = split_num(num, split)
             new_num.append(next_num)
    else: 
        if snail_num >= 10 and split == False: 
            odd_add = 0
            if (snail_num % 2) != 0: odd_add = 1
            snail_num = [snail_num // 2, snail_num // 2 + odd_add]
            split = True
        return snail_num, split
    return new_num, split


def reduce(snail_num):
    print(snail_num)
    snail_num, exploded = explode(snail_num)
    if exploded: 
        print("exploded")
        print(snail_num, "\n")
        return reduce(snail_num)
    snail_num, split = split_num(snail_num)
    if split: 
        print("splited")
        print(snail_num, "\n")
        return reduce(snail_num)
    return snail_num


# snail_num = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
snail_num = [[[[0,7],4],[15,[0,13]]],[1,1]]
# snail_num = [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]

reduced = reduce(snail_num)
# reduced = reduce(test_split_snail_num)
print(reduced)
