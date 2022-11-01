import heapq


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
    if row < 0:
        return False
    return True


def is_down_inbounds(row, total_rows):
    if row + 1 >= total_rows:
        return False 
    return True


def is_right_inbounds(column, total_columns):
    if column  + 1 >= total_columns:
        return False
    return True


def is_left_inbounds(column):
    if column < 0:
        return False
    return True


def initialize_priority_queue():
    # priority queue structure (risk_level, (row, column))
    pq = [(0, (0,0))]
    heapq.heapify(pq)
    print(pq)
    return pq


def find_path(input_arr, risk_arr, pq):
    total_rows = len(input_arr)
    total_columns = len(input_arr[0])
    end_row, end_column = find_end_point(input_arr)
    visited = []
    while len(pq) > 0:
        risk, (row,column) = heapq.heappop(pq)
        print(f"risk of {risk}, at row: {row} column: {column}")

        # if been here before, dont try again
        if (row, column) in visited:
            continue
        visited.append((row, column))

        # if at end, return risk
        if (row, column) == (end_row, end_column):
            break
        # explore arr
        if is_right_inbounds(column, total_columns):
            right_risk = risk + input_arr[row][column + 1]
            right_coords = (row, column + 1)
            right = (right_risk, right_coords)
            heapq.heappush(pq, right)
        if is_down_inbounds(row, total_rows):
            down_risk = risk + input_arr[row + 1][column]
            down_coords = (row + 1, column)
            down = (down_risk, down_coords)
            heapq.heappush(pq, down)
    return risk


input_arr = parse_input_to_arr("input_01.txt")
# for line in input_arr:
#     print(line)

risk_arr = create_risk_arr(input_arr)
# for line in risk_arr:
#     print(line)

pq = initialize_priority_queue()

final_risk = find_path(input_arr, risk_arr, pq)
print(final_risk)