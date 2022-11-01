import re
import numpy as np

line_points = []
with open('input.txt') as file:
    lines = file.read().splitlines();
    coordinate_regex = re.compile('\d,\d')
    for line in lines:
        line_split = line.split()
        start_point_list = line_split[0].split(',')
        end_point_list = line_split[2].split(',')
        start_point_tuple = (int(start_point_list[0]), int(start_point_list[1]))
        end_point_tuple = (int(end_point_list[0]), int(end_point_list[1]))
        line_points.append([start_point_tuple, end_point_tuple])

max_x = 0
max_y = 0
for points in line_points:
    for point in points:
        if point[0] > max_x: max_x = point[0]
        if point[1] > max_y: max_y = point[1]

grid = np.zeros((max_x + 1, max_y + 1))
# grid = np.zeros((1000,1000))

def is_horizontal(points): 
    if points[0][1] == points[1][1]: return True
    return False

def is_vertical(points):
    if points[0][0] == points[1][0]: return True
    return False

for points in line_points:
    if is_horizontal(points):
        if points[0][0] > points[1][0]:
            greater_x = points[0][0]
            lesser_x = points[1][0]
        else:
            greater_x = points[1][0]
            lesser_x = points[0][0]
        while (lesser_x <= greater_x):
            grid[lesser_x][points[0][1]] += 1
            lesser_x += 1
    elif is_vertical(points):
        if points[0][1] > points[1][1]:
            greater_y = points[0][1]
            lesser_y = points[1][1]
        else:
            greater_y = points[1][1]
            lesser_y = points[0][1]
        while (lesser_y <= greater_y):
            grid[points[0][0]][lesser_y] += 1
            lesser_y += 1
    else:
        x1 = points[0][0]
        y1 = points[0][1]
        x2 = points[1][0]
        y2 = points[1][1]
        x_increment = True if x1 < x2 else False
        y_increment = True if y1 < y2 else False
        if x_increment:
            while(x1 <= x2):
                grid[x1][y1] += 1
                x1 += 1
                if y_increment: y1 += 1
                else: y1 -= 1
        else:
            while(x1 >= x2):
                grid[x1][y1] += 1
                x1 -= 1
                if y_increment: y1 += 1
                else: y1 -= 1


                

flipped_grid = np.swapaxes(grid, 0, 1)

count = 0
for row in flipped_grid:
    for num in row:
        if num >= 2: count += 1

print(flipped_grid)
print(count)