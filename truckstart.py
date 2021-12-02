def truckstart(petrolpumps):
    st=0
    rt=starttruck(st,petrolpumps)
    return rt

def starttruck(st,petrolpumps):
    for i in range(st,len(petrolpumps)):
        if (petrolpumps[i][0]>petrolpumps[i][1]):
            st=i
            break
    pv=petrolpumps[st][0]-petrolpumps[st][1]
    flag=True
    for i in range((st+1),len(petrolpumps)):
        pv=(pv+petrolpumps[i][0])-petrolpumps[i][1]
        if pv<0:
            flag=False
            break
    if(flag):
        for i in range(0,st):
            pv=(pv+petrolpumps[i][0])-petrolpumps[i][1]
            if pv<0:
                flag=False
                break
    if(flag):
        print(pv)
        return st
    else:
        return starttruck((st+1),petrolpumps)
if(__name__=="__main__"):
    n=int(input())
    petrolpumps=[]
    for i in range(n):
        petrolpumps.append(list(map(int,input().rstrip().split())))

    result=truckstart(petrolpumps)
    print(result)
            
        
        
