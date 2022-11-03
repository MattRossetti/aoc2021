import numpy
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
    count = 0
    if binary_string[:1] != 0:
        while last_bit_flag == False:
            index = 5 * (count)
            next_bit_chunk = binary_string[index:index + 5]
            bits += next_bit_chunk[1:]
            if next_bit_chunk[:1] == "0":
                last_bit_flag = True
            count += 1
    else:
        bits = binary_string[:5]
    literal_value = int(bits, 2)
    return literal_value


def find_bit_chunks(literal_value):
    literal_value_binary = f"{literal_value:b}"
    # print("literal value binary", literal_value_binary)
    binary_digits = len(literal_value_binary)
    bit_chunks = (binary_digits - 1) // 4 + 1
    # print("bit chunks", bit_chunks)
    return bit_chunks

def remove_literal_values(binary_string, bit_chunks):
    # print("FINDING LITERAL FOR ", binary_string)
    for _ in range(bit_chunks):
        binary_string = binary_string[5:]
    if "1" not in binary_string:
        return ""
    # print("FINDING LITERAL FOR ", binary_string)
    return binary_string


def parse_length_type_id(binary_string):
    length_id = int(binary_string[:1])
    return length_id


def remove_length_type_id(binary_string):
    binary_string = binary_string[1:]
    return binary_string


def get_zero_type_sub_packet_length(binary_string):
    sub_packet_length_binary = binary_string[:15]
    sub_packet_length = int(sub_packet_length_binary, 2)
    return sub_packet_length


def remove_zero_type_sub_packet_length(binary_string):
    binary_string = binary_string[15:]
    return binary_string


def get_one_type_sub_packet_count(binary_string):
    sub_packet_count_binary = binary_string[:11]
    sub_packet_count = int(sub_packet_count_binary, 2)
    return sub_packet_count


def remove_one_type_sub_packet_count(binary_string):
    binary_string = binary_string[11:]
    return binary_string


def parse_hex_to_binary(hex_input):
    bin_digits = len(hex_input) * 4
    binary_string = bin(int(hex_input, 16))[2:].zfill(bin_digits)
    # print(f"starting Binary String: {binary_string}")
    return binary_string


def decode_binary_string(binary_string, answer=0,
    sub_packet_operator = -1,
    in_length_packet=False, length=0, length_max=0, 
    in_count_packet=False, count=0, count_max=0,
    current_sub_packet_values=[]):
    length_one = len(binary_string)

    print("IN LOOP", binary_string)
    packet_version = parse_packet_version(binary_string)
    binary_string = remove_packet_version(binary_string)
    # print(f"packet version: {packet_version}")

    length_diff = 0
    type_id = parse_type_id(binary_string)
    binary_string = remove_type_id(binary_string)
    print(f"type id: {type_id}")
    if type_id == 4:
        literal_value = process_literal_values(binary_string)
        bit_chunks = find_bit_chunks(literal_value)
        binary_string = remove_literal_values(binary_string, bit_chunks)
        length_two = len(binary_string)
        length_diff = length_one - length_two
        print(f"literal value: {literal_value}")
        current_sub_packet_values.append(literal_value)

    if in_count_packet == True:
        count += 1
        print("count_max: ", count_max)
        print("count: ", count)
        print("sub_packet_operator: ", sub_packet_operator)
        if count == count_max:
            print()
            print("here_count")
            print(current_sub_packet_values)
            if sub_packet_operator == 0:
                answer = numpy.sum(current_sub_packet_values)
            if sub_packet_operator == 1:
                answer = numpy.product(current_sub_packet_values)
            if sub_packet_operator == 2:
                answer = min(current_sub_packet_values)
            if sub_packet_operator == 3:
                answer = max(current_sub_packet_values)
            count = 0
            if sub_packet_operator == 5:
                if current_sub_packet_values[0] > current_sub_packet_values[1]:
                    answer = 1
                else:
                    answer = 0
            if sub_packet_operator == 6:
                if current_sub_packet_values[0] < current_sub_packet_values[1]:
                    answer = 1
                else:
                    answer = 0
            if sub_packet_operator == 7:
                if current_sub_packet_values[0] == current_sub_packet_values[1]:
                    answer = 1
                else:
                    answer = 0
            print("ANSWER: ", answer, "OPERATOR: ", sub_packet_operator)
            count = 0
            current_sub_packet_values = []
            in_count_packet = False
    
    if in_length_packet == True:
        length += length_diff
        print("length_max: ", length_max)
        print("length:", length)
        print("sub_packet_operator", sub_packet_operator)
        if length >= length_max:
            print()
            print("here_len")
            print(current_sub_packet_values)
            if sub_packet_operator == 0:
                answer = numpy.sum(current_sub_packet_values)
            if sub_packet_operator == 1:
                answer = numpy.product(current_sub_packet_values)
            if sub_packet_operator == 2:
                answer = min(current_sub_packet_values)
            if sub_packet_operator == 3:
                answer = max(current_sub_packet_values)
            if sub_packet_operator == 5:
                if current_sub_packet_values[0] > current_sub_packet_values[1]:
                    answer = 1
                else:
                    answer = 0
            if sub_packet_operator == 6:
                if current_sub_packet_values[0] < current_sub_packet_values[1]:
                    answer = 1
                else:
                    answer = 0
            if sub_packet_operator == 7:
                if current_sub_packet_values[0] == current_sub_packet_values[1]:
                    answer = 1
                else:
                    answer = 0
            print("ANSWER: ", answer, "OPERATOR: ", sub_packet_operator)
            current_sub_packet_values = []
            length = 0
            in_length_packet = False
    
    if type_id != 4:
        length_type_id = parse_length_type_id(binary_string)
        binary_string = remove_length_type_id(binary_string)
        print(f"length type id: {length_type_id}")

        if length_type_id == 0:
            zero_type_sub_packet_length = get_zero_type_sub_packet_length(binary_string)
            binary_string = remove_zero_type_sub_packet_length(binary_string)
            binary_sub_string = binary_string[:zero_type_sub_packet_length]
            binary_string = binary_string[zero_type_sub_packet_length:]
            print(f"zero type sub packet length: {zero_type_sub_packet_length}")
            in_length_packet = True
            length_max = zero_type_sub_packet_length
            sub_packet_operator = type_id
            return decode_binary_string(binary_sub_string, answer, 
                in_length_packet=in_length_packet,
                length=length,
                length_max=length_max,
                in_count_packet=in_count_packet,
                count=count,
                count_max=count_max,
                current_sub_packet_values=current_sub_packet_values,
                sub_packet_operator=sub_packet_operator
                )

        if length_type_id == 1:
            one_type_sub_packet_count = get_one_type_sub_packet_count(binary_string)
            print(f"one type sub packet count: {one_type_sub_packet_count}")
            binary_string = remove_one_type_sub_packet_count(binary_string)
            in_count_packet = True
            count_max = one_type_sub_packet_count
            sub_packet_operator = type_id


    # print("end_loop_bs", binary_string)
    print()
    if len(binary_string) > 0 and "1" in binary_string:
        return decode_binary_string(binary_string, answer, 
        in_length_packet=in_length_packet,
        length=length,
        length_max=length_max,
        in_count_packet=in_count_packet,
        count=count,
        count_max=count_max,
        current_sub_packet_values=current_sub_packet_values,
        sub_packet_operator=sub_packet_operator
        )

    return answer

# print(process_literal_values(bin_example))
# hex_input = "68A"
# hex_input = "D2FE28"
# hex_input = "38006F45291200"
# hex_input = "EE00D40C823060"
# hex_input = "8A004A801A8002F478"
# hex_input = "620080001611562C8802118E34"
# hex_input = "C0015000016115A2E0802F182340"
# hex_input = "A0016C880162017C3686B18A3D4780"

# hex_input = "420D5A802122FD25C8CD7CC010B00564D0E4B76C7D5A59C8C014E007325F116C958F2C7D31EB4EDF90A9803B2EB5340924CA002761803317E2B4793006E28C2286440087C5682312D0024B9EF464DF37EFA0CD031802FA00B4B7ED2D6BD2109485E3F3791FDEB3AF0D8802A899E49370012A926A9F8193801531C84F5F573004F803571006A2C46B8280008645C8B91924AD3753002E512400CC170038400A002BCD80A445002440082021DD807C0201C510066670035C00940125D803E170030400B7003C0018660034E6F1801201042575880A5004D9372A520E735C876FD2C3008274D24CDE614A68626D94804D4929693F003531006A1A47C85000084C4586B10D802F5977E88D2DD2898D6F17A614CC0109E9CE97D02D006EC00086C648591740010C8AF14E0E180253673400AA48D15E468A2000ADCCED1A174218D6C017DCFAA4EB2C8C5FA7F21D3F9152012F6C01797FF3B4AE38C32FFE7695C719A6AB5E25080250EE7BB7FEF72E13980553CE932EB26C72A2D26372D69759CC014F005E7E9F4E9FA7D3653FCC879803E200CC678470EC0010E82B11E34080330D211C663004F00101911791179296E7F869F9C017998EF11A1BCA52989F5EA778866008D8023255DFBB7BD2A552B65A98ECFEC51D540209DFF2FF2B9C1B9FE5D6A469F81590079160094CD73D85FD2699C5C9DCF21F0700094A1AC9EDA64AE3D37D34200B7B401596D678A73AFB2D0B1B88057230A42B2BD88E7F9F0C94F1ECB7B0DD393489182F9802D3F875C00DC40010F8911C61F8002111BA1FC2E400BEA5AA0334F9359EA741892D81100B83337BD2DDB4E43B401A800021F19A09C1F1006229C3F8726009E002A12D71B96B8E49BB180273AA722468002CC7B818C01B04F77B39EFDF53973D95ADB5CD921802980199CF4ADAA7B67B3D9ACFBEC4F82D19A4F75DE78002007CD6D1A24455200A0E5C47801559BF58665D80"

# hex_input = "C200B40A82"
# hex_input = "04005AC33890"
# hex_input = "880086C3E88112"
# hex_input = "CE00C43D881120"
# hex_input = "D8005AC2A8F0"
# hex_input = "F600BC2D8F"
hex_input = "9C0141080250320F1802104A08"

binary_string = parse_hex_to_binary(hex_input)
answer = decode_binary_string(binary_string)
print("answer: ", answer)