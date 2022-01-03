inputs = []
outputs = []

with open('input.txt') as file:
    lines = file.readlines()
    for line in lines:
        split_line = line.split('|')
        line_inputs = split_line[0].split()
        inputs.append(line_inputs)
        line_outputs = split_line[1].split()
        outputs.append(line_outputs)
        
empty_dict = {
    'a':None,
    'b':None,
    'c':None,
    'd':None,
    'e':None,
    'f':None,
    'g':None,
}
all_number_match_dicts = []
empty_number_match_dict = {
    '0':None,
    '1':None,
    '2':None,
    '3':None,
    '4':None,
    '5':None,
    '6':None,
    '7':None,
    '8':None,
    '9':None,
}

reference_dicts = []
for i in range(len(inputs)):
    input_dict = empty_dict.copy()
    reference_dicts.append(input_dict)
    sorted_input = sorted(inputs[i], key=len)

    # print('sorted', sorted_input)

    for char in sorted_input[1]:
        if char in sorted_input[0]: continue
        input_dict['a'] = char
    
    possible_threes = [sorted_input[3], sorted_input[4], sorted_input[5]]
    index_of_three = None
    for i in range(len(possible_threes)):
        match_to_one_count = 0
        for char in possible_threes[i]:
            if char in sorted_input[0]: match_to_one_count += 1
        # print(match_to_one_count)
        if match_to_one_count == 2: index_of_three = 3 + i
    
    # print('i_3', index_of_three)
    
    for char in sorted_input[2]:
        if char in sorted_input[0]: continue
        if char in sorted_input[index_of_three]: continue
        input_dict['b'] = char
    
    for char in sorted_input[2]:
        if char in sorted_input[0]: continue
        if char == input_dict['b']: continue
        input_dict['d'] = char

    possible_fives = possible_threes.copy()
    # print('p5', possible_fives)
    possible_fives.remove(possible_fives[index_of_three - 3])
    # print('p5-3', possible_fives)

    five = None
    for possible_five in possible_fives:
        for char in possible_five:
            if char == input_dict['b']: five = possible_five
    # print('five', five)
    
    for char in five:
        if char == input_dict['a']: continue
        if char == input_dict['b']: continue
        if char == input_dict['d']: continue
        if char in sorted_input[0]: continue
        input_dict['g'] = char
        
    for char in five:
        if char == input_dict['a']: continue
        if char == input_dict['b']: continue
        if char == input_dict['d']: continue
        if char == input_dict['g']: continue
        input_dict['f'] = char

    chars_but_e_for_six = ''
    for key in input_dict:
        if input_dict[key] == None: continue
        chars_but_e_for_six += input_dict[key]
    
    possible_twos = possible_fives.copy()
    two = None
    for possible_two in possible_twos:
        if possible_two == five: continue
        two = possible_two
    
    for char in sorted_input[index_of_three]:
        if char == input_dict['a']: continue
        if char == input_dict['d']: continue
        if char == input_dict['g']: continue
        if char == input_dict['f']: continue
        input_dict['c'] = char
    
    for char in two:
        if char == input_dict['a']: continue
        if char == input_dict['c']: continue
        if char == input_dict['d']: continue
        if char == input_dict['g']: continue
        input_dict['e'] = char
    
    number_match_dict = empty_number_match_dict.copy()
    
    number_match_dict['0'] = input_dict['a'] + input_dict['b'] + input_dict['c'] + input_dict['e'] + input_dict['f'] + input_dict['g']
    number_match_dict['1'] = input_dict['c'] + input_dict['f']
    number_match_dict['2'] = input_dict['a'] + input_dict['c'] + input_dict['d'] + input_dict['e'] + input_dict['g']
    number_match_dict['3'] = input_dict['a'] + input_dict['c'] + input_dict['d'] + input_dict['f'] + input_dict['g']
    number_match_dict['4'] = input_dict['b'] + input_dict['c'] + input_dict['d'] + input_dict['f']
    number_match_dict['5'] = input_dict['a'] + input_dict['b'] + input_dict['d'] + input_dict['f'] + input_dict['g']
    number_match_dict['6'] = input_dict['a'] + input_dict['b'] + input_dict['d'] + input_dict['e'] + input_dict['f'] + input_dict['g']
    number_match_dict['7'] = input_dict['a'] + input_dict['c'] + input_dict['f']
    number_match_dict['8'] = input_dict['a'] + input_dict['b'] + input_dict['c'] + input_dict['d'] + input_dict['e'] + input_dict['f'] + input_dict['g']
    number_match_dict['9'] = input_dict['a'] + input_dict['b'] + input_dict['c'] + input_dict['d'] + input_dict['f'] + input_dict['g']

    for key in number_match_dict:
        sorted_value_list = sorted(number_match_dict[key])
        value_string = ''
        for char in sorted_value_list:
            value_string += char
        number_match_dict[key] = value_string
    
    all_number_match_dicts.append(number_match_dict)

sorted_outputs = []
for output in outputs:
    temp_output = []
    for digit in output:
        sorted_digit_list = sorted(digit)
        sorted_digit = ''
        for char in sorted_digit_list:
            sorted_digit += char
        temp_output.append(sorted_digit)
    sorted_outputs.append(temp_output)

sum = 0
for i in range(len(sorted_outputs)):
    temp_num = ''
    # print(all_number_match_dicts[i])
    # print(sorted_outputs[i])
    # print(all_number_match_dicts[i])
    for digit in sorted_outputs[i]:
        for match_key in all_number_match_dicts[i]:
            if all_number_match_dicts[i][match_key] == digit: temp_num += match_key
    print(temp_num)
    sum += int(temp_num)

print('sum', sum)

# print(len(sorted_outputs), len(all_number_match_dicts), len(inputs))


