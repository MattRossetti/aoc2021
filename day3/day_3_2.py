diagnostic_codes = []
with open('input.txt') as file:
    lines = file.read().splitlines()
    for line in lines:
        diagnostic_codes.append(line)

def find_oxygen_rating(codes, current_position): 
    zero_counter = 0
    one_counter = 0
    most_common = ''
    
    ##base case
    if len(codes) == 1:
        return codes[0]

    for code in codes:
        if code[current_position] == '0': zero_counter += 1
        else: one_counter += 1
    
    #find most common
    if zero_counter > one_counter: most_common = '0'
    elif one_counter > zero_counter: most_common = '1'
    else: most_common = 'tie'

    ##create new codes array
    filtered_codes = []
    if most_common == 'tie':
        #find  with 1 in current_position
        for code in codes:
            if code[current_position] == '1':
                filtered_codes.append(code)

    else:
        for code in codes:
            if code[current_position] == most_common:
                filtered_codes.append(code)
    
    return(find_oxygen_rating(filtered_codes, current_position + 1))

def find_co2_rating(codes, current_position): 
    zero_counter = 0
    one_counter = 0
    least_common = ''
    
    ##base case
    if len(codes) == 1:
        return codes[0]

    for code in codes:
        if code[current_position] == '0': zero_counter += 1
        else: one_counter += 1
    
    #find most common
    if zero_counter < one_counter: least_common = '0'
    elif one_counter < zero_counter: least_common = '1'
    else: least_common = 'tie'


    ##create new codes array
    filtered_codes = []
    if least_common == 'tie':
        #find  with 1 in current_position
        for code in codes:
            if code[current_position] == '0':
                filtered_codes.append(code)

    else:
        for code in codes:
            if code[current_position] == least_common:
                filtered_codes.append(code)
    
    return(find_co2_rating(filtered_codes, current_position + 1))


oxygen_rating_binary = find_oxygen_rating(diagnostic_codes, 0)
co2_rating_binary = find_co2_rating(diagnostic_codes, 0)
# print(oxygen_rating_binary, co2_rating_binary)
oxygen_rating = int(oxygen_rating_binary, 2)
co2_rating = int(co2_rating_binary, 2)
# print(oxygen_rating, co2_rating, type(oxygen_rating), type(co2_rating))
print(oxygen_rating * co2_rating)
