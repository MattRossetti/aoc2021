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

total = 0
count_if_len = [2, 3, 4, 7]
for output in outputs:
    for pattern in output:
        if len(pattern) in count_if_len: total += 1

print(total)



