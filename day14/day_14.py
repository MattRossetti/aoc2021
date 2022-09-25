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


def grow_polymer(polymer, pair_list): 
    new_polymer = ''
    for i, char in enumerate(polymer):
        try:
            polymer_pair = char + polymer[i + 1]
        except IndexError:
            new_polymer += char
            break
        for pair in pair_list:
            if pair[0] == polymer_pair:
                polymer_pair = polymer_pair[0] + pair[1]
                break 
        new_polymer += polymer_pair
    return new_polymer


def grow_polymer_n_times(polymer, pair_list, n):
    for i in range(n):
        start_time = time.time()
        polymer = grow_polymer(polymer, pair_list)
        elapsed_time = time.time() - start_time
        print(f'grew polymer {i + 1} times in {round(elapsed_time, 4)} seconds')
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

polymer, pair_list = make_puzzle_inputs('input_1.txt')
polymer = grow_polymer_n_times(polymer, pair_list, 25)
occurance_dict = create_occurance_dict(polymer)
print(occurance_dict)
max_key, min_key = find_max_and_min_key(occurance_dict)
answer = calculate_answer(occurance_dict, min_key, max_key)
print(f'answer = {answer}')
