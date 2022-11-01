# Knowns
## First Three bits encode 'packet version'
## Second three bits encode the 'type ID'
### Type ID '4' represents a literal value
#### Literal Values, take 5 nums, ignore first, thats binary num
def parse_packet_version(binary_string):
    packet_version_binary = binary_string[:3]
    packet_version = int(packet_version_binary, 2)
    return packet_version


def remove_packet_version(binary_string):
    binary_string = binary_string[3:]
    return binary_string


def parse_type_id(binary_string):
    type_id_binary = binary_string[:3]
    type_id = int(type_id_binary, 2)
    return type_id


def remove_type_id(binary_string):
    binary_string = binary_string[3:]
    return binary_string


def process_literal_values(binary_string):
    last_bit_flag = False
    bits = ""
    while last_bit_flag == False:
        next_bit_chunk = binary_string[:5]
        bits += next_bit_chunk
        binary_string = binary_string[5:0]
        if next_bit_chunk[0] == 0:
            last_bit_flag == True
            # strip remaining zeros
            binary_string = binary_string[3:]
    literal_values = int(bits, 2)


def remove_literal_values(binary_string):
    # take away binary string changes from above function


            




def process_hex_input(hex_input):
    binary_string = bin(int(hex_input, 16))[2:]
    print(f"Starting Binary String: {binary_string}")
    while len(binary_string) > 0:
        packet_version = parse_packet_version(binary_string)
        binary_string = remove_packet_version(binary_string)
        type_id = parse_type_id(binary_string)
        binary_string = remove_type_id(binary_string)
        if type_id == 4:
            process_literal_values(binary_string)
        break
    print(binary_string, packet_version, type_id)


hex_input = "D2FE28"

process_hex_input(hex_input)