diagnostic_codes = []
with open('input.txt') as file:
    lines = file.read().splitlines()
    for line in lines:
        diagnostic_codes.append(line)

code_length = len(diagnostic_codes[0])
bit_tracker = []
gamma_rate = ''
epsilon_rate = ''

for i in range(code_length):
    bit_tracker.append([0,0])

for code in diagnostic_codes:
    for i in range(len(code)):
        if int(code[i]) == 0: bit_tracker[i][0] += 1
        else: bit_tracker[i][1] += 1

for i in range(code_length):
    if bit_tracker[i][0] > bit_tracker[i][1]:
        gamma_rate += '0'
        epsilon_rate += '1'
    else:
        gamma_rate += '1'
        epsilon_rate += '0'

print(bit_tracker)
print(gamma_rate)
print(int(gamma_rate, 2) * int(epsilon_rate, 2))



