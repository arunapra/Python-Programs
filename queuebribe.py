def minimumBribes(q):
    # Write your code here
    nb=0
    nb=bsort(q,nb)
    if(nb):
        print(nb)
    
def bsort(q,nb):
    j=1
    for i in range(len(q)):
        if (i+1)<len(q):
            if(q[i]-j)>2:
                print("Too chaotic")
                return None
            if (q[i]>q[i+1]):
                q[i],q[i+1]=q[i+1],q[i]
                nb+=1
            j+=1
    if(q==sorted(q)):
        return nb
    else:
        return bsort(q,nb)
                
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
