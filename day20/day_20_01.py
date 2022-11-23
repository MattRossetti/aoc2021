def get_input(input_file):
    with open(input_file) as file:
        lines = file.read().splitlines()
    algo_string = ""
    input_toggle = False
    input = []
    for line in lines:
        if input_toggle is False:
            algo_string += line
        else:
            input.append(line)
        if line == "":
            input_toggle = True
    return algo_string, input


def resize_for_enhancement(input):
    height = len(input)
    length = len(input[0])
    new_height = height + 120
    new_length = length + 120
    image = []
    for i in range(new_height):
        row = ""
        for j in range(new_length):
            if (i >= 60 and i < new_height - 60) and (j >= 60 and j < new_length - 60):
                row += input[i - 60][j - 60]
            else:
                row += "."
        image.append(row)
    return image


# def resize_for_enhancement(input):
#     height = len(input)
#     length = len(input[0])
#     new_height = height + 8
#     new_length = length + 8
#     image = []
#     for i in range(new_height):
#         row = ""
#         for j in range(new_length):
#             if (i >= 4 and i < new_height-4) and (j >= 4 and j < new_length - 4):
#                 row += input[i - 4][j - 4]
#             else:
#                 row += "."
#         image.append(row)
#     return image


def find_pixel_string(new_image, x, y):
    pixel_string = ""
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if new_image[i][j] == ".":
                pixel_string += "0"
            else:
                pixel_string += "1"
    return pixel_string


def enhance_image(image, algo_string):
    new_image = []
    for i in range(len(image)):
        new_row = ""
        for j in range(len(image[0])):
            new_row += "."
        new_image.append(new_row)
    for i in range(len(new_image)):
        new_image[i] = list(new_image[i])
        if i == 0 or i == len(new_image) - 1:
            new_image[i] = "".join(new_image[i])
            continue
        for j in range(len(new_image[0])):
            if j == 0 or j == len(new_image[0]) - 1:
                continue
            pixel_string = find_pixel_string(image, i, j)
            pixel_string_int = int(pixel_string, 2)
            enhanced_char = algo_string[pixel_string_int]
            # print(pixel_string, int(pixel_string, 2), enhanced_char)
            new_image[i][j] = enhanced_char
        new_image[i] = "".join(new_image[i])
    return new_image


def enhance_n_times(image, algo_string, n):
    for i in range(n):
        print(i)
        # for row in image:
        #     print(row)
        image = resize_for_enhancement(image)
        image = enhance_image(image, algo_string)
    #     print()
    # for row in image:
    #     print(row)
    return image


def count_lit_pixels(image):
    lit_count = 0
    for row in image:
        for pixel in row:
            if pixel == "#":
                lit_count += 1
    return lit_count


def resize_for_count(image, n):
    trim_number = (60 * n) - (2*n)
    resized_image = []
    for i, row in enumerate(image):
        if i <= trim_number or i >= (len(image) - trim_number):
            continue
        row = row[trim_number:(trim_number * -1)]
        resized_image.append(row)
    # print()
    # for row in resized_image:
    #     print(row)
    return resized_image


algo_string, input = get_input("day_20_01_input.txt")
# algo_string, input = get_input("day_20_example_input.txt")
print(algo_string)
print()
# for line in input:
#     print(line)

image = enhance_n_times(input, algo_string, 50)
image = resize_for_count(image, 50)
lit_pixels = count_lit_pixels(image)
print("ANSWER")
print("\t", lit_pixels)

# print()
# image = resize_for_enhancement(input)
# for line in image:
#     print(line)
#
# image = enhance_image(image, algo_string)
# print()
# for row in image:
#     print(row)
