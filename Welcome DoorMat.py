# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=input().split()
n=int(n)
m=int(m)
s=".|."
j=1
for i in range(n):
    if n//2==i:
        print("WELCOME".center(m,"-"))
    elif i<n//2:
        print((s*j).center(m,"-"))
        j+=2
    else:
        j-=2
        print((s*j).center(m,"-"))
        
