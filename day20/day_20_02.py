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


def grow_image(image, n):
    row_add_string = ""
    for _ in range(len(image[0]) + n * 2):
        row_add_string += "."
    small_row_add_string = "." * n
    for i, row in enumerate(image):
        image[i] = small_row_add_string + row + small_row_add_string
    for _ in range(n):
        image.insert(0, row_add_string)
        image.append(row_add_string)
    return image


def find_enhanced_char(image, x, y, algo_string):
    pixel_string = ""
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            try:
                char = image[i][j]
            except IndexError:
                char = "."
            if char == "#":
                pixel_string += "1"
            else:
                pixel_string += "0"
    pixel_string_int = int(pixel_string, 2)
    new_char = algo_string[pixel_string_int]
    return new_char


def enhance_image(image, algo_string):
    new_row = "." * len(image[0])
    new_image = [new_row for _ in range(len(image))]
    for i, row in enumerate(image):
        new_image[i] = list(new_image[i])
        for j, char in enumerate(row):
            enhanced_char = find_enhanced_char(image, i, j, algo_string)
            new_image[i][j] = enhanced_char
        new_image[i] = "".join(new_image[i])
    return new_image


def count_lit_pixels(image):
    lit_count = 0
    for i, row in enumerate(image):
        if i == 0:
            continue
        for pixel in row:
            if pixel == "#":
                lit_count += 1
    return lit_count


def print_image(image):
    for row in image:
        print(row)
    print()


def enhance_image_n_times(image, n, algo_string):
    for i in range(n):
        print(i)
        # print_image(image)
        image = enhance_image(image, algo_string)
    # print_image(image)
    return image


def trim_image(image, n):
    for _ in range(n):
        image = image[1:]
        image.pop()
    for i, _ in enumerate(image):
        image[i] = image[i][n:-n]
    return image


algo_string, image = get_input("day_20_01_input.txt")
# algo_string, image = get_input("day_20_example_input.txt")
print(algo_string)
print_image(image)
image = grow_image(image, 500)
image = enhance_image_n_times(image, 50, algo_string)
image = trim_image(image, 100)
answer = count_lit_pixels(image)
print("ANSWER")
print("\t", answer)
