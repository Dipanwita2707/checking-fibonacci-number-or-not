# Checking input number is Fibonacci Number or not:

import math
def perfectSquare(x):
    s=int(math.sqrt(x)) #to check square function
    return s*s==x
a=input("enter the number to check: ").split(" ")  #taking input
b=[]
c=[]
for i in a:
    if i.isdigit():
        b.append(i)
for j in b:
    c.append(int(j))
for k in c:
    result1=(5*(k**2))+4 # 1st Formula to check Fibonacci number
    result2=(5*(k**2))-4 # 2nd Formula to check Fibonacci number
    if perfectSquare(result1) or perfectSquare(result2):
        print(k,"is a fibonacci number")
    else:
        print(k,"is not a fibonacci number")



