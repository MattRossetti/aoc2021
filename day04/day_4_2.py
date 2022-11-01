import pandas as pd

bingo_numbers = []
bingo_boards_raw = []
with open('input.txt') as file:
    bingo_numbers = file.readline().split(',')
    file.readline()
    bingo_boards_raw = file.read().splitlines()

bingo_boards = []
bingo_board = []
board_marks = []
for line in bingo_boards_raw:
    if line != '':
        bingo_board.append(line.split())
    if len(bingo_board) == 5:        
        # df_bingo_board = pd.DataFrame(bingo_board)
        bingo_boards.append(bingo_board)
        bingo_board = []
        board_marks.append([])

def update_board_marks(number):
    for board_id in range(len(bingo_boards)):
        # print(board_id)
        for y in range(len(bingo_boards[board_id])):
            # print(bingo_boards[board_id][y])
            for x in range(len(bingo_boards[board_id][y])):
                # print(bingo_boards[board_id][y][x])
                if int(bingo_boards[board_id][y][x]) == number:
                    board_marks[board_id].append((x,y))

bingo_win_conditions = [
    [(0,0), (1,0), (2,0), (3,0), (4,0)],
    [(0,1), (1,1), (2,1), (3,1), (4,1)],
    [(0,2), (1,2), (2,2), (3,2), (4,2)],
    [(0,3), (1,3), (2,3), (3,3), (4,3)],
    [(0,4), (1,4), (2,4), (3,4), (4,4)],
    [(0,0), (0,1), (0,2), (0,3), (0,4)],
    [(1,0), (1,1), (1,2), (1,3), (1,4)],
    [(2,0), (2,1), (2,2), (2,3), (2,4)],
    [(3,0), (3,1), (3,2), (3,3), (3,4)],
    [(4,0), (4,1), (4,2), (4,3), (4,4)],
]

def check_for_wins():
    winners = []
    for win_condition in bingo_win_conditions:
        for i in range(len(board_marks)):
            count = 0
            for coord in win_condition:
                if coord not in board_marks[i]: break
                count += 1
            if count == 5: winners.append(i)
    return winners 


winners_list = []
final_number = None
count = 0

for i in range(len(bingo_numbers)):
    count += 1
    update_board_marks(int(bingo_numbers[i]))
    winners = check_for_wins()
    for winner in winners:
        if winner not in winners_list: winners_list.append(winner)
        if len(winners_list) == 100:
            final_number = bingo_numbers[i]
            print(final_number)
            break
    if final_number != None: break

print(winners_list, len(winners_list), final_number)

print(bingo_boards[winners_list[99]])

unmarked_numbers = []
for x in range(len(bingo_boards[winners_list[99]])):
    for y in range(len(bingo_boards[winners_list[99]][x])):
        if ((x,y)) not in board_marks[winners_list[99]]:
            unmarked_numbers.append(int(bingo_boards[winners_list[99]][y][x]))

unmarked_total = 0
for number in unmarked_numbers:
    unmarked_total += number

print(int(unmarked_total) * int(final_number))