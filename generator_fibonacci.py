def fib(n):
    p,q=0,1
    while(p<n):
        yield p
        p,q=q,p+q

n=int(input())
for i in fib(n):
    print(i,end=" ")

