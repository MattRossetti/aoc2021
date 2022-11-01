import random
from datetime import datetime
import seaborn as sns


def parse_input_to_arr(input_file_path):
    with open(input_file_path) as file:
        lines = file.read().splitlines()
        input_arr = []
        for line in lines:
            line_arr = []
            for char in line:
                line_arr.append(int(char))
            input_arr.append(line_arr)
        return input_arr


def find_end_point(input_arr):
    end_row = len(input_arr) - 1
    end_column = len(input_arr[0]) - 1
    return (end_row, end_column)


def current_risk_level(input_arr, row, column):
    return int(input_arr[row][column])


def is_up_out_of_bounds(row):
    if row < 0:
        return True
    return False


def is_down_out_of_bounds(row, total_rows):
    if row + 1 > total_rows:
        return True
    return False


def is_right_out_of_bounds(column, total_columns):
    if column  + 1 > total_columns:
        return True
    return False


def is_left_out_of_bounds(column):
    if column < 0:
        return True
    return False


def random_walk(
    input_arr,
    end_row,
    end_column,
    total_rows,
    total_columns,
    row=0,
    column=0,
    visited=[],
    score=0,
):
    # update score
    if row == 0 and column == 0: visited = []
    score += input_arr[row][column]
    # update where I've been (visited)
    visited.append([row, column])
    # if at end return score
    if row == end_row and column == end_column:
        # print(f"found end with score {score}")
        return score
    # which directions can I move?
    ## don't allow out of bounds
    moves = []
    # if is_up_out_of_bounds(row - 1) == False:
    #     moves.append([row - 1, column])
    if is_down_out_of_bounds(row + 1, total_rows) == False:
        moves.append([row + 1, column])
    if is_right_out_of_bounds(column + 1, total_columns) == False:
        moves.append([row, column + 1])
    # if is_left_out_of_bounds(column - 1) == False:
    #     moves.append([row, column - 1])

    ## don't allow a spot I've already been
    for i, move in enumerate(moves):
        if move in visited:
            moves[i] = None
    moves = list(filter(None, moves))
    # if no moves allowed return 0
    if len(moves) == 0:
        return 0
    # randomly pick direction
    next_move_index = random.randint(0, len(moves) - 1)
    next_move = moves[next_move_index]

    return random_walk(
        input_arr,
        end_row,
        end_column,
        total_rows,
        total_columns,
        next_move[0],
        next_move[1],
        visited,
        score,
    )


input_arr = parse_input_to_arr("input_01.txt")
end_row, end_column = find_end_point(input_arr)
total_rows = len(input_arr)
total_columns = len(input_arr)
# score = random_walk(input_arr, end_row, end_column, total_rows, total_columns)
# print(score)
good_scores_list = []
start_time = datetime.now()
for i in range(100):
    scores_list = []
    for j in range(10000):
        found_score = random_walk(input_arr, end_row, end_column, total_rows, total_columns)
        if found_score == 0: continue
        scores_list.append(found_score)
    good_scores_list.append(min(scores_list))

end_time = datetime.now()
print(f"run time = {(end_time - start_time).total_seconds()}")
# print(good_scores_list)
print(min(good_scores_list))

sns.histplot(good_scores_list)