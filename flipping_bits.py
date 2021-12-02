n=int(input("Enter a number:"))
s=str(bin(n))[2::]
print(s)
znum = s.zfill(32)
print(znum)
fnum=""
for i in range(len(znum)):
    if znum[i]=="1":
        fnum=fnum+"0"
    else:
        fnum=fnum+"1"
print(fnum)
k=fb=0
for j in range(len(fnum)-1,-1,-1):
    fb=fb+int(fnum[j])*pow(2,k)
    k=k+1
print(fb)
        
