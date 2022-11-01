import heapq
import pandas as pd


def parse_input_to_arr(input_file_path):
    with open(input_file_path) as file:
        lines = file.read().splitlines()
        input_arr = []
        for line in lines:
            line_arr = []
            for char in line:
                line_arr.append(int(char))
            input_arr.append(line_arr)
        return(input_arr)


def five_times_input(input_arr):
    original_rows = len(input_arr)
    original_columns = len(input_arr[0])
    final_arr = [ [0] * original_columns * 5 for _ in range(original_rows * 5)] 
    final_rows = len(final_arr)
    final_columns = len(final_arr[0])
    print(final_rows, final_columns)
    
    for i in range(final_rows):
        grid_id_row_shift = i // original_rows
        for j in range(final_columns):
            grid_id_row  = i % original_rows
            grid_id_column = j % original_columns
            grid_id = (j // original_columns)
            lookup_id = (grid_id + grid_id_row_shift) 
            next_num = input_arr[grid_id_row][grid_id_column] + lookup_id
            if next_num > 9:
                next_num = next_num - 9
            final_arr[i][j] = next_num
    
    return final_arr

def find_end_point(input_arr):
    end_row = len(input_arr) - 1    
    end_column = len(input_arr[0]) - 1
    return (end_row, end_column)


def current_risk_level(input_arr, row, column):
    return int(input_arr[row][column])


def create_risk_arr(input_arr):
    rows = len(input_arr)
    columns = len(input_arr[0])
    risk_arr = [ [0] * columns for _ in range(rows)]
    return risk_arr


def is_up_inbounds(row):
    if row <= 0:
        return False
    return True


def is_down_inbounds(row, total_rows):
    if row + 1 >= total_rows:
        return False 
    return True


def is_left_inbounds(column):
    if column <= 0:
        return False
    return True


def is_right_inbounds(column, total_columns):
    if column  + 1 >= total_columns:
        return False
    return True


def initialize_priority_queue():
    # priority queue structure (risk_level, (row, column))
    pq = [(0, (0,0))]
    heapq.heapify(pq)
    print(pq)
    return pq


def find_path(input_arr, pq):
    total_rows = len(input_arr)
    total_columns = len(input_arr[0])
    end_row, end_column = find_end_point(input_arr)
    visited = set()
    count = 0
    while len(pq) > 0:
        count += 1
        # print(count)
        risk, (row,column) = heapq.heappop(pq)
        # print(f"risk of {risk}, at row: {row} column: {column}")

        # if been here before, dont try again
        if (row, column) in visited:
            # print("been here")
            continue
        visited.add((row, column))

        # if at end, return risk
        if (row, column) == (end_row, end_column):
            break
        # explore arr
        if is_right_inbounds(column, total_columns):
            right_risk = risk + input_arr[row][column + 1]
            right_coords = (row, column + 1)
            right = (right_risk, right_coords)
            heapq.heappush(pq, right)
        if is_left_inbounds(column):
            left_risk = risk + input_arr[row][column - 1]
            left_coords = (row, column - 1)
            left = (left_risk, left_coords)
            heapq.heappush(pq, left)
        if is_down_inbounds(row, total_rows):
            down_risk = risk + input_arr[row + 1][column]
            down_coords = (row + 1, column)
            down = (down_risk, down_coords)
            heapq.heappush(pq, down)
        if is_up_inbounds(row):
            up_risk = risk + input_arr[row - 1][column]
            up_coords = (row - 1,column)
            up = (up_risk, up_coords)
            heapq.heappush(pq, up)
    return risk


input_arr = parse_input_to_arr("input_01.txt")
# for line in input_arr:
#     print(line)


pq = initialize_priority_queue()


final_arr = five_times_input(input_arr)
# final_arr_csv = pd.DataFrame(final_arr).to_csv("final_arr_dump.txt", index=False, header=False)
# final_arr_csv = pd.DataFrame(final_arr).to_csv("final_arr_index.txt", index=False, header=False)

# for line in final_arr:
#     print(line)

final_risk = find_path(final_arr, pq)
print(final_risk)
