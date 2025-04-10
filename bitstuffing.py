def bit_stuffing(data):
    """Perform bit stuffing on input binary data."""
    stuffed_data = []
    count = 0
    for bit in data:
        stuffed_data.append(bit)
        if bit == '1':
            count += 1
            if count == 5:
                stuffed_data.append('0')
                count = 0
        else:
            count = 0
    return ''.join(stuffed_data)

def bit_unstuffing(stuffed_data):
    """Reverse bit stuffing to get original data."""
    unstuffed_data = []
    count = 0
    for bit in stuffed_data:
        if bit == '1':
            count += 1
            unstuffed_data.append(bit)
        else:
            if count == 5:
                count = 0
                continue
            unstuffed_data.append(bit)
            count = 0
    return ''.join(unstuffed_data)

def byte_stuffing(data, flag='F', escape='E'):
    """Perform byte stuffing on input string data."""
    stuffed_data = ""
    for byte in data:
        if byte in [flag, escape]:
            stuffed_data += escape
        stuffed_data += byte
    return stuffed_data

def byte_unstuffing(stuffed_data, flag='F', escape='E'):
    """Reverse byte stuffing to get original data."""
    unstuffed_data = ""
    skip = False
    for i in range(len(stuffed_data)):
        if skip:
            skip = False
            continue
        if stuffed_data[i] == escape:
            skip = True
        unstuffed_data += stuffed_data[i]
    return unstuffed_data

bit_data = input("Enter a binary string for bit stuffing: ")
stuffed_bit_data = bit_stuffing(bit_data)
unstuffed_bit_data = bit_unstuffing(stuffed_bit_data)

print("\nBit Stuffing:")
print("Original :", bit_data)
print("Stuffed :", stuffed_bit_data)
print("Unstuffed :", unstuffed_bit_data)

byte_data = input("\nEnter a string for byte stuffing: ")
flag_char = input("Enter the flag character (default: 'F'): ") or 'F'
escape_char = input("Enter the escape character (default: 'E'): ") or 'E'

stuffed_byte_data = byte_stuffing(byte_data, flag_char, escape_char)
unstuffed_byte_data = byte_unstuffing(stuffed_byte_data, flag_char, escape_char)

print("\nByte Stuffing:")
print("Original :", byte_data)
print("Stuffed :", stuffed_byte_data)
print("Unstuffed :", unstuffed_byte_data)