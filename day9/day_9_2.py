import pygame
import sys
import pandas as pd
import math
from collections import defaultdict

input_depths = []

with open('input.txt') as file:
    rows = file.readlines()
    for row in rows:
        row_list = []
        for digit in row:
            if  digit == '\n': break
            row_list.append(digit)
        input_depths.append(row_list)

input_depths_df = pd.DataFrame(input_depths)
plot_colors_df = input_depths_df.copy()
(row_count, col_count) = input_depths_df.shape
print(f'{row_count} rows X {col_count} cols matrix')

def check_if_lower_than_neighbors(row_index, col_index):
    is_top_edge = False
    is_left_edge = False
    is_bottom_edge = False
    is_right_edge = False
    if (row_index - 1) < 0: is_top_edge = True
    if (col_index - 1) < 0: is_left_edge = True
    if (row_index + 1) > 4: is_bottom_edge = True
    if (col_index + 1) > 9: is_right_edge = True
    value_to_check = input_depths_df.iat[row_index, col_index]
    if not is_top_edge:
        if input_depths_df.iat[row_index - 1, col_index] <= value_to_check: return
    if not is_left_edge:
        if input_depths_df.iat[row_index, col_index - 1] <= value_to_check: return
    if not is_bottom_edge:
        if input_depths_df.iat[row_index + 1, col_index] <= value_to_check: return
    if not is_right_edge:
        if input_depths_df.iat[row_index, col_index + 1] <= value_to_check: return
    # return (row_index, col_index)
    plot_colors_df.values[row_index, col_index] = 10
    return (row_index, col_index, input_depths_df.iat[row_index,col_index])

local_bottoms = []
for row_index in range(row_count):
    for col_index in range(col_count):
        # print(f'row = {row_index}, col = {col_index}')
        possible_bottom = check_if_lower_than_neighbors(row_index, col_index)
        if possible_bottom == None: continue
        local_bottoms.append(possible_bottom)

basin_df = pd.DataFrame(index = range(row_count), columns = range(col_count))
basin_count = 0

def update_basin_df(basins_to_compare):
    if len(basins_to_compare) == 0:
        global basin_count
        basin_count += 1
        return basin_count
    if len(basins_to_compare) == 1: return int(basins_to_compare[0])

    compare_basin_size = []
    for basin in basins_to_compare:
        this_basin_size = 0
        for row_index in range(row_count):
            for col_index in range(col_count):
                if basin_df.iat[row_index, col_index] == basin:
                    this_basin_size += 1
        compare_basin_size.append(this_basin_size)
    
    max_basin_size = max(compare_basin_size)
    max_basin_index = compare_basin_size.index(max_basin_size)
    basin_to_keep = basins_to_compare[max_basin_index]
    basins_to_replace = basins_to_compare.copy()
    basins_to_replace.remove(basin_to_keep)

    for basin_remove in basins_to_replace:
        for row_index in range(row_count):
            for col_index in range(col_count):
                if basin_df.iat[row_index, col_index] == basin_remove:
                    basin_df.values[row_index, col_index] = int(basin_to_keep)
    
    return int(basin_to_keep)



def find_basin_id(row_index, col_index):
    if int(input_depths_df.values[row_index, col_index]) == 9:
        basin_df.values[row_index, col_index] = float('nan')
        return

    is_top_edge = False
    is_left_edge = False
    is_bottom_edge = False
    is_right_edge = False
    if (row_index - 1) < 0: is_top_edge = True
    if (col_index - 1) < 0: is_left_edge = True
    if (row_index + 1) > 4: is_bottom_edge = True
    if (col_index + 1) > 9: is_right_edge = True
    basins_to_compare = []
    if not is_top_edge:
        if not math.isnan(basin_df.iat[row_index - 1, col_index]):
            basins_to_compare.append(basin_df.iat[row_index - 1, col_index])
    if not is_left_edge:
        if not math.isnan(basin_df.iat[row_index, col_index - 1]):
            basins_to_compare.append(basin_df.iat[row_index, col_index - 1])
    if not is_bottom_edge:
        if not math.isnan(basin_df.iat[row_index + 1, col_index]):
            basins_to_compare.append(basin_df.iat[row_index + 1, col_index])
    if not is_right_edge:
        if not math.isnan(basin_df.iat[row_index, col_index + 1]):
            basins_to_compare.append(basin_df.iat[row_index, col_index + 1])
    
    basin_df.values[row_index, col_index] = update_basin_df(basins_to_compare)
    

for row_index in range(row_count):
    for col_index in range(col_count):
        print(row_index, col_index)
        find_basin_id(row_index, col_index)


# print(basin_df)

basin_dict = defaultdict()
for row_index in range(row_count):
    for col_index in range(col_count):
        basin_id = basin_df.iat[row_index, col_index]
        if math.isnan(basin_id): continue
        try:
            basin_dict[basin_id] += 1
        except KeyError:
            basin_dict[basin_id] = 1


sorted_basin_dict = {}
sorted_basin_keys = sorted(basin_dict, reverse = True, key=basin_dict.get)
for key in sorted_basin_keys:
    sorted_basin_dict[key] = basin_dict[key]

print(sorted_basin_dict)


# BLOCKSIZE = 10
# SCREEN_WIDTH = col_count * BLOCKSIZE
# SCREEN_HEIGHT = row_count * BLOCKSIZE
# # GREYSCALE = [
# #     (33, 33, 33),
# #     (66, 66, 66),
# #     (97, 97, 97),
# #     (117, 117, 117),
# #     (158, 158, 158),
# #     (189, 189, 189),
# #     (224, 224, 224),
# #     (238, 238, 238),
# #     (245, 245, 245),
# #     (250, 250, 250),
# #     (239, 71, 111),
# # ]
# GREYSCALE = [
#     (33, 33, 33),
#     (66, 66, 66),
#     (97, 97, 97),
#     (117, 117, 117),
#     (158, 158, 158),
#     (189, 189, 189),
#     (224, 224, 224),
#     (238, 238, 238),
#     (245, 245, 245),
#     (255, 127, 17),
#     (239, 71, 111),
# ]
# WHITE = (255, 255, 255)
# CYAN = (0, 200, 200)
# BLACK = (0, 0, 0)
# RED = (239, 71, 111)
# BORDER_COLOR = (226, 219, 190)


# pygame.init()
# number_font = pygame.font.SysFont( None, int(BLOCKSIZE * 1.5))
# SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("AOC Day 9 visualization")

# SCREEN.fill(BLACK)

# def drawGrid():
#     x_count = 0
#     for x in range(0, SCREEN_WIDTH, BLOCKSIZE):
#         y_count = 0
#         for y in range(0, SCREEN_HEIGHT, BLOCKSIZE):
#             depth = int(input_depths_df.iat[y_count, x_count])
#             color = int(plot_colors_df.iat[y_count, x_count])
#             rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
#             pygame.draw.rect(SCREEN, BORDER_COLOR, rect, 1)
#             number_text = f' {str(depth)} '
#             number_image = number_font.render(number_text, True, CYAN, GREYSCALE[color])
#             SCREEN.blit(number_image, (x, y ))
#             y_count += 1
#         x_count += 1

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     drawGrid()
#     pygame.display.update()
