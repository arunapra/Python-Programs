def binsrch(a,x,low,high):
    if(low>high):
        return(-1)
    mid=(low+high)//2
    if(a[mid]==x):
        return mid
    elif(x<a[mid]):
        high=mid-1
    else:
        low=mid+1
    return binsrch(a,x,low,high)

n=int(input("Enter the number of elements in the array:"))
a=list(map(int,input().split()))
x=int(input("Enter the element to be searched:"))
a.sort()
print(binsrch(a,x,0,len(a)-1))
