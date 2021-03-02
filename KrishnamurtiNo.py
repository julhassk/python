num = int(input("Enter any number:"))
temp = num
f = 1
sum1 = 0

while(num>0):
    r = int(num%10)
    f = 1
    for x in range(1,r+1):
        f = f*x
        sum1 = sum1 + f
        num = num/10

if (sum1 == temp):
    print(temp,"is a krishnamurti number")
else:
    print(temp,"is not krishnamurti number")

    '''
    output:
    Enter any number:145
    145 is a krishnamurti number
    '''