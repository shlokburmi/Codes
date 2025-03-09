hex2 = "2FABCA7428AC358E629C"     
n = int(input("Enter the number, data to be divided: "))
a = []
s = ""
for i in range(len(hex2)):
    s += hex2[i]
    if (i + 1) % (len(hex2) // n) == 0:
        a.append(s)
        s = ""
if s:
    a.append(s)
print("Divided Parts:", a)
def checksum():
    total_sum = 0
    for part in a:
        num = int(part, 16)
        total_sum += num
    return total_sum
def carry():
    sum_val = checksum()
    while sum_val > 0xFFFF:
        carry_part = sum_val >> 16  
        sum_val = (sum_val & 0xFFFF) + carry_part  
    return sum_val
def ones_complement(bit_length=16):
    num = carry()
    bitmask = (1 << bit_length) - 1  
    ones_comp = num ^ bitmask  
    return hex(ones_comp)
print("---------------------SENDER--------------------")
print("Checksum:", hex(checksum()))
print("Final Sum after Carry:", hex(carry()))  
print("One's Complement of Sum:", ones_complement())
a1=str(ones_complement()) # converting a hexadecimal number into string
a1=a1.upper() #for uppercase
a1=a1[2:] #for splitting the 0x from hexadecimal number
a.append(a1) #for appendig the checksum in the list 
print("---------------------RECEIVER------------------")
print("After appending the checksum in the list:-\n",a)
print("Sum:", hex(checksum()))
print("Final Sum after Carry:", hex(carry()))
print("One's Complement of Sum at the receiver side :", ones_complement())
print("SINCE WE ARE GETTING 0x0 , the CHECKSUM we calculated was correct !!")