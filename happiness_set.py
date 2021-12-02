# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=input().split()
n=int(n)
m=int(m)
iarr=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))
hap=0
for i in range(n):
    if iarr[i] in A:
        hap+=1
    elif iarr[i] in B:
        hap-=1
print(hap)
