def sortf(arr):
    s=[]
    for k in range(len(arr)):
        min=1000
        for i in range(len(arr)):
            if(arr[i]<min):
                min=arr[i]
        s.append(min)
        del arr[arr.index(min)]
    return s

n=list(map(int,input().split()))
print(sortf(n))
    