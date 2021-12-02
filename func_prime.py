def primef(n):
    if n==1:
        return False
    else:
        for i in range(2,n//2):
            if(n%i==0):
                return False
        return True

#n=int(input())
pl=[]
for i in range(1,101):
    if(primef(i)):
        pl.append(i)
print(pl)