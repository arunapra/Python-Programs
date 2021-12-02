# Enter your code here. Read input from STDIN. Print output to STDOUT
num=int(input())
stri=[]
for i in range(num):
    stri.append(str(input()))
for j in range(num):
    length=len(stri[j])
    evenstr=""
    oddstr=""
    for k in range(length):
        if k%2==0:
            evenstr+=stri[j][k]
        else:
            oddstr+=stri[j][k]
    print(evenstr,oddstr)
