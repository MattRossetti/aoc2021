import copy


def puzzle_input(input_file_path):
    with open(input_file_path) as file:
        dot_coords = [] 
        instruction_list = []
        instructions = False
        for line in file.read().splitlines():
            if line == '': 
                instructions = True 
                continue
            if instructions == False: dot_coords.append(line.split(','))
            else: instruction_list.append(line.split()[-1].split('=')) 
    return (dot_coords, instruction_list)


def convert_coords_to_int(dot_coords, instruction_list):
    for coord in dot_coords:
        coord[0] = int(coord[0])
        coord[1] = int(coord[1])
    for instruction in instruction_list:
        instruction[1] = int(instruction[1])
    return dot_coords, instruction_list


def create_dot_map(dot_coords):
    x_max = 0
    y_max = 0
    for coords in dot_coords: 
        if (coords[0]) > x_max: x_max = (coords[0])
        if (coords[1]) > y_max: y_max = (coords[1])
    x_list = []
    dot_map = []
    for _ in range(x_max + 1):
        x_list.append('.')
    for _ in range(y_max + 1):
        dot_map.append(copy.deepcopy(x_list))
    return dot_map 


def populate_dot_map(dot_coords, dot_map):
    for coord in dot_coords: dot_map[coord[1]][coord[0]] = '#'
    return dot_map


def vertical_fold(dot_map, col_to_fold):
    for row in dot_map:
        for dot_index in range(col_to_fold + 1, len(row)): 
            if row[dot_index] != '#': continue
            fold_index = col_to_fold - (dot_index - col_to_fold)
            row[fold_index] = '#'
    for row in dot_map:
        del row[col_to_fold:]
    return dot_map
            

def horizontal_fold(dot_map, row_to_fold):
    for i in range(len(dot_map)):
        if i != row_to_fold: continue
        for row_index in range(row_to_fold + 1, len(dot_map)):
            fold_index = row_to_fold - (row_index - row_to_fold)
#            print(f'fold_index = {fold_index}, row_index = {row_index}')
            new_arr = ['.' for _ in range(len(dot_map[row_index]))]
            for j in range(len(new_arr)):
                if dot_map[row_index][j] == '#' or dot_map[fold_index][j] == '#':
                    new_arr[j] = '#'
            dot_map[fold_index] = new_arr
        break 
    del dot_map[row_to_fold:]
    return dot_map


def fold_dot_map(dot_map, instruction):
    if instruction[0] == 'x':
        dot_map = vertical_fold(dot_map, instruction[1])
    elif instruction[0] == 'y':
        dot_map = horizontal_fold(dot_map, instruction[1])
    return dot_map


def print_dot_map(dot_map):
    for row in dot_map:
        print(row)
    print()
    return


def perform_folds(dot_map, instruction_list):
    for instruction in instruction_list:
        dot_map = fold_dot_map(dot_map, instruction)
    return dot_map


def count_dots(dot_map):
    dot_count = 0
    for row in dot_map:
        for char in row:
            if char == '#': dot_count += 1
    return dot_count


# dot_coords, instruction_list = puzzle_input('example1.txt')
dot_coords, instruction_list = puzzle_input('input.txt')
dot_coords, instruction_list = convert_coords_to_int(dot_coords, instruction_list)
dot_map = create_dot_map(dot_coords)
dot_map = populate_dot_map(dot_coords, dot_map)

print_dot_map(dot_map)
# dot_map = fold_dot_map(dot_map, instruction_list[0])
dot_map = perform_folds(dot_map, instruction_list)
print_dot_map(dot_map)
dot_count = count_dots(dot_map)
print(f'final dot count: {dot_count}')
