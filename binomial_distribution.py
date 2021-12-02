# Enter your code here. Read input from STDIN. Print output to STDOUT
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
        
def comb(n,x):
    return fact(n)/(fact(x)*fact(n-x))

def binomial_d(x,n,p):
    return comb(n,x)*p**x*(1-p)**(n-x)

p,q=input().split()
p=float(p)
q=float(q)
odds= p/q

print(round(sum([binomial_d(i,6,odds/(1+odds)) for i in range(3,7)]),3))
