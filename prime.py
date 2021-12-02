# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def prime(n):
    if (n==1):
        return False
    
    for i in range(2,math.floor(math.sqrt(n))+1):
        if (n%i==0):
            return False
    return True
t=int(input())
n=[]
for i in range(t):
    n.append(int(input()))
for i in range(t):
    p=prime(n[i])
    if p==True:
        print("Prime")
    else:
        print("Not prime")
