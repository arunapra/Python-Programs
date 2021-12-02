def logdec(func):
    def funcwrap(*args):
        print(args)
        return func(*args)
    return funcwrap

@logdec
def fib(start,second,n):
    print(start)
    c=0
    while(c<n):
        start,second=second,start+second
        c+=1
        print(start)

start=int(input())
second=int(input())
n=int(input())
fib(start,second,n)