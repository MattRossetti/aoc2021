from collections import defaultdict
import time

def split_pair(pair):
    pair = pair.split(' -> ')
    return pair


def make_puzzle_inputs(file_path):
    with open(file_path) as file:
        input_text = file.read().splitlines()
        polymer = input_text[0]
        pair_list = input_text[2:]
        pair_list = list(map(split_pair, pair_list))
        return polymer, pair_list 


def grow_polymer(polymer, pair_list, polymer_lookup_dict): 
    new_polymer = ''
    updated_polymer_pair = ''
    for i, char in enumerate(polymer):
        try:
            polymer_pair = char + polymer[i + 1]
        except IndexError:
            new_polymer += char
            break
        if polymer_pair in polymer_lookup_dict.keys():
            updated_polymer_pair = polymer_lookup_dict[polymer_pair]
        else:
            for pair in pair_list:
                if pair[0] == polymer_pair:
                    updated_polymer_pair = polymer_pair[0] + pair[1]
                    polymer_lookup_dict[polymer_pair] = updated_polymer_pair
                    break 
        new_polymer += updated_polymer_pair
    return new_polymer, polymer_lookup_dict


def grow_polymer_n_times(polymer, pair_list, polymer_lookup_dict, n):
    for i in range(n):
        print('NNC' in polymer)
        start_time = time.time()
        polymer, polymer_lookup_dict = grow_polymer(polymer, pair_list, polymer_lookup_dict)
        elapsed_time = time.time() - start_time
        print(f'grew polymer {i + 1} times in {round(elapsed_time, 4)} seconds')
        # occurance_dict = create_occurance_dict(polymer)
        # max_key, min_key = find_max_and_min_key(occurance_dict)
        # print(occurance_dict)
        # answer = calculate_answer(occurance_dict, min_key, max_key)
        # print(f'polymer is {len(polymer)} characters')
        # print(f'answer is {answer}')
    return polymer


def default_to_0():
    return 0


def create_occurance_dict(polymer):
    occurance_dict = defaultdict(default_to_0)
    for char in polymer:
        occurance_dict[char] = occurance_dict[char] + 1
    return dict(occurance_dict)


def find_max_and_min_key(occurance_dict):
    max_key = max(occurance_dict, key=occurance_dict.get)
    min_key = min(occurance_dict, key=occurance_dict.get)
    return max_key, min_key


def calculate_answer(occurance_dict, min_key, max_key):
    max = occurance_dict[max_key]
    min = occurance_dict[min_key]
    return max - min

polymer, pair_list = make_puzzle_inputs('example_1.txt')
polymer_lookup_dict = {}
polymer = grow_polymer_n_times(polymer, pair_list, polymer_lookup_dict, 17)
occurance_dict = create_occurance_dict(polymer)
print(occurance_dict)
max_key, min_key = find_max_and_min_key(occurance_dict)
answer = calculate_answer(occurance_dict, min_key, max_key)
print(f'answer = {answer}')
