# Enter your code here. Read input from STDIN. Print output to STDOUT

X=int(input())
s=input().split()
size=list(map(int,s))
cust_num=int(input())

total=0
for i in range(cust_num):
    sz,price=input().split()
    sz=int(sz)
    price=int(price)
    for j in range(len(size)):
        if sz==size[j]:
            total=total+price
            del size[j]
            break
print(total) 
