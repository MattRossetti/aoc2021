## works for example but does not scale up to input, need to implement path finding algorithm
from datetime import datetime

def parse_input_to_arr(input_file_path):
    with open(input_file_path) as file:
        lines = file.read().splitlines()
        input_arr = []
        for line in lines:
            line_arr = []
            for char in line:
                line_arr.append(char)
            input_arr.append(line_arr)
        return(input_arr)

def find_end_point(input_arr):
    end_row = len(input_arr) - 1    
    end_column = len(input_arr[0]) - 1
    return (end_row, end_column)

def traverse_path(input_arr, end_point, current_risk_level=0, risk_levels=[], 
    row_index=0, column_index=0):
    # out of bounds?
    if row_index > end_point[0]: return
    if column_index > end_point[1]: return
    # add risk
    current_risk_level += int(input_arr[row_index][column_index])
    # current risk already to high?
    if len(risk_levels) > 0:
        min_risk_level = min(risk_levels)
        if current_risk_level > min_risk_level:
            return
    # found end?
    if (row_index, column_index) == end_point:
        print(f'found end! with risk level:{current_risk_level}')
        risk_levels.append(current_risk_level)
    # try right
    traverse_path(input_arr, end_point, current_risk_level, risk_levels, 
        row_index, column_index + 1)
    # try down
    traverse_path(input_arr, end_point, current_risk_level, risk_levels,
        row_index + 1, column_index)
    return min(risk_levels)

input_arr = parse_input_to_arr("example_01.txt")
# input_arr = parse_input_to_arr("input_01.txt")
end_point = find_end_point(input_arr)
start_time = datetime.now()
lowest_risk_level = traverse_path(input_arr, end_point)
end_time = datetime.now()
print(f'run time = {end_time - start_time}')
print(lowest_risk_level)
