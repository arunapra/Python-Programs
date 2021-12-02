x=[2,4,6,8]
y={i:i**2 for i in x}
z=[i**2 for i in x]
print(z)
print(y)
l=list(map(lambda i:i**3,x))
print(l)
print("-------------------------------")
a=[1,2,3]
b=[4,5,6]
print(list(zip(a,b)))
cl=[(x+y) for x,y in zip(a,b)]
print(cl)
