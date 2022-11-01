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


def current_risk_level(input_arr, row, column):
    return int(input_arr[row][column])


def find_best_path(input_arr, current_row=0, current_column=0, path_id=0, path_history={}):
    # am i out of bounds?
    if current_row + 1 > len(input_arr): return
    if current_row < 0: return
    if current_column + 1 > len(input_arr[0]): return
    if current_column < 0: return
    # have i been here before?
    if bool(path_history) == True:
        if (current_row, current_column) in path_history[path_id - 1]["history"]: return
    # initialize/update risk_level and history
    if bool(path_history) == False:
        path_history[path_id] = {
            "risk_level": 0, 
            "history": [(current_row, current_column)]
        }
    else:
        history = path_history[path_id - 1]["history"]
        history.append((current_row, current_column))
        risk_level = path_history[path_id - 1]["risk_level"] + current_risk_level(input_arr, current_row, current_column)
        path_history[path_id] = {
            "risk_level": risk_level,
            "history": history
        }
    # am i at end?
    if (current_row, current_column) == find_end_point(input_arr):
        print("WE MADE IT")
        print(path_history[path_id]["history"])
        exit()
        return path_history[path_id]["risk_level"]
    # find next node to traverse
    next_node = min(path_history, key=lambda x: path_history[x]["risk_level"])
    next_node_row, next_node_column = path_history[next_node]["history"][-1]
    print(next_node)
    # traverse neighboring nodes
    ## traverse right
    find_best_path(input_arr, next_node_row, next_node_column + 1, path_id + 1) 
    ## traverse down
    find_best_path(input_arr, next_node_row + 1, next_node_column, path_id + 1) 
    ## traverse left
    find_best_path(input_arr, next_node_row, next_node_column - 1, path_id + 1) 
    ## traverse up
    find_best_path(input_arr, next_node_row - 1, next_node_column, path_id + 1) 
    return "failed"

input_arr = parse_input_to_arr("example_01.txt")
# for line in input_arr:
#     print(line)
risk_level = find_best_path(input_arr)
print(risk_level)
