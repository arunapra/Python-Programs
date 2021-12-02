T=int(input())
for j in range(T):
    N,k=map(int,input().split())
    s=input()
    t=0
    for i in range(N//2):
        if(s[i]!=s[N-(i+1)]):
            t+=1
    if(t==k):
        print(f"Case #{j+1}: 0")
    elif(t<k):
        d=k-t
        print(f"Case #{j+1}: {d}")
    else:
        d=t-k
        print(f"Case #{j+1}: {d}")


