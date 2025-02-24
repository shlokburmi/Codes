# a=["1010101","1110001","1101011","1010111","11001100",""] #for even parity 
n = int(input("Enter the number of rows: "))
a = []
print("Enter each binary string for the array:")
for i in range(n):
    a.append(input(f"Row {i+1}: "))
def func(z):
    for i in range(len(a)-1):
        c=0
        for j in range(len(a[i])):
            if(a[i][j]=='1'):
                c=c+1
                # print(a[i][j])
        if(z==1):
            if(c%2==0):
                a[i]+='0'
            else:
                a[i]+='1'
        elif(z==2):
            if(c%2!=0):
                a[i]+='0'
            else:
                a[i]+='1'
        else:
            print("errorrrr ; enter your choice:")
            break
    for i in range(0,len(a[0])):
        c=0
        for j in range(0,len(a)-1):
            if(a[j][i]=='1'):
                c=c+1
        if(z==1):
            if(c%2==0):
                a[-1]+='0'
            else:
                a[-1]+='1'
        elif(z==2):
            if(c%2!=0):
                a[-1]+='0'
            else:
                a[-1]+='1'
        else:
            print("errorrrr ; enter your choice:")
            break
    return a
print("For source")
print("1.Press for Even Parity:")
print("2.Press for Odd Parity:")
i1=int(input("Enter your choice:"))
func(i1)
print("For reciever")
print("1.Press for Even Parity verification:")
print("2.Press for Odd Parity verification:")
i2=int(input("Enter your choice:"))
if(i1==i2):
    a=func(i1)
    print(a)
else:
    print("receiver is making wrong parity")