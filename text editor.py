# Enter your code here. Read input from STDIN. Print output to STDOUT
q=int(input())
opt=[]
bapp=[]
deleted=[]
s=""
for i in range(q):
    n=input().split()
    opt.append(n[0])
    if(n[0]=="1"):
        bapp.append(s)
        s=s+n[1]
    elif(n[0]=="2"):
        k=len(s)-int(n[1])
        deleted.append(s[k:])
        s=s[0:k]
    elif(n[0]=="3"):
        print(s[int(n[1])-1])
    elif(n[0]=="4"):
        for j in range(len(opt)-1,0,-1):
            if(opt[j]=="1"):
                s=bapp[-1]
                bapp.pop()
                del opt[j]
                break
            elif(opt[j]=="2"):
                s=s+deleted[-1]
                deleted.pop()
                del opt[j]
                break
