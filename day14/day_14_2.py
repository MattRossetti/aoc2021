from collections import Counter


def create_next_pairs_dict(pair_list_raw):
    next_pairs_dict = {}
    for pair in pair_list_raw:
        pair = pair.split(' -> ')
        next_pairs_dict[pair[0]] = [pair[0][0] + pair[1], pair[1] + pair[0][1]]
    return next_pairs_dict
    

def make_puzzle_inputs(file_path):
    with open(file_path) as file:
        input_text = file.read().splitlines()
        polymer = input_text[0]
        next_pairs_dict = create_next_pairs_dict(input_text[2:])
    return polymer, next_pairs_dict


def create_starting_pair_counts(polymer, next_pairs_list):
    pair_counts = Counter()
    for i, _ in enumerate(polymer):
        if i + 1 == len(polymer): break
        next_pairs = next_pairs_list[polymer[i:i+2]]
        pair_counts.update(next_pairs)
    return pair_counts


def update_pair_counts(pair_counts, next_pairs_list):
    new_pair_counts = Counter()
    for key, value in pair_counts.items():
        update_dict_1 = {next_pairs_list[key][0]: value}
        update_dict_2 = {next_pairs_list[key][1]: value}
        new_pair_counts.update(update_dict_1)
        new_pair_counts.update(update_dict_2)
    return new_pair_counts


def grow_polymer(polymer, next_pairs_list, n):
    print(0)
    pair_counts = create_starting_pair_counts(polymer, next_pairs_list)
    print(1)
    for i in range(n - 1):
        print(i + 2)
        pair_counts = update_pair_counts(pair_counts, next_pairs_list)
    char_counts = Counter()
    for key, value in pair_counts.items():
        update_dict_1 = {key[0]: value}
        update_dict_2 = {key[1]: value}
        char_counts.update(update_dict_1)
        char_counts.update(update_dict_2)
    answer_dict = {}
    for key, value in char_counts.items():
        extra = 0
        if key == polymer[0] or key == polymer[-1]: 
            extra = .5 
        answer_dict[key] = value / 2 + extra
    return answer_dict


def find_max_and_min_key(answer_dict):
    max_key = max(answer_dict, key=answer_dict.get)
    min_key = min(answer_dict, key=answer_dict.get)
    return max_key, min_key


def calculate_answer(answer_dict, min_key, max_key):
    max = answer_dict[max_key]
    min = answer_dict[min_key]
    return max - min


polymer, next_pairs_list = make_puzzle_inputs('input_1.txt')
pair_counts = create_starting_pair_counts(polymer, next_pairs_list)
pair_counts = update_pair_counts(pair_counts, next_pairs_list)
answer_dict = grow_polymer(polymer, next_pairs_list, 40)
max_key, min_key = find_max_and_min_key(answer_dict)
answer = calculate_answer(answer_dict, min_key, max_key)
print(answer_dict)
print(f'answer = {answer}')
