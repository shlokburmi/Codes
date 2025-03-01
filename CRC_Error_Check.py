deg=int(input("Enter the degree of Polynomial: "))
arr=[]
no=[1,0,1,0,1,0,1,0,1,0]  
for i in range(deg,-1,-1):
    j = int(input(f"Coefficient of x power {i} is: "))
    arr.append(j)

zeros = [0] * deg
no1=no+zeros
def polynomial_division(dividend, divisor):
    dividend = list(dividend)
    divisor = list(divisor)
    divisor_len = len(divisor)
    for i in range(len(dividend) - divisor_len + 1):
        if dividend[i] == 1:
            for j in range(divisor_len):
                dividend[i + j] ^= divisor[j]  # XOR operation

    return dividend[len(dividend) - divisor_len + 1:]
print("Dividend",no1)
print("Divisor",arr)
d=polynomial_division(no1,arr)
print("CRC",d)
print("--------------------------------------")
print("For Receiver Side:- ")
no1=no+d
print("Dividend",no1)
print("Divisor",arr)
rec=polynomial_division(no1,arr)
if(sum(rec) == 0):
    print("No error ")
else:
    print("Error found")