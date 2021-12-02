''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
from itertools import combinations
def findanotherhc(i,hc,start_road,end_road,dist):
    if i in start_road and i in end_road:
        idx=start_road.index(i)
        dc=end_road[idx]
        if dc!=hc:
            idx=end_road.index(i)
            dc=start_road[idx]
        if dc==hc:
            dist+=1
            return dist
    if i in start_road:
        idx=start_road.index(i)
        dc=end_road[idx]
        if dc==hc:
            dist+=1
            return dist
        if end_road.count(dc)==1:
            if dc in start_road:
                if start_road.count(dc)==1:
                    idx=start_road.index(dc)
                    dc=end_road[idx]
                    if(dc==hc):
                        dist+=1
                        return dist
                    else:
                        return 0
                else:
                    dist+=1
                    return findanotherhc(dc,hc,start_road,end_road,dist)
            else:
                return 0
        dist+=1
        return findanotherhc(dc,hc,start_road,end_road,dist)
    elif i in end_road:
        idx=end_road.index(i)
        dc=start_road[idx]
        if dc==hc:
            dist+=1
            return dist
        if start_road.count(dc)==1:
            if dc in end_road:
                if end_road.count(dc)==1:
                    idx=end_road.index(dc)
                    dc=start_road[idx]
                    if(dc==hc):
                        dist+=1
                        return dist
                    else:
                        return 0
                else:
                    dist+=1
                    return findanotherhc(dc,hc,start_road,end_road,dist)
            else:
                return 0
        dist+=1
        return findanotherhc(dc,hc,start_road,end_road,dist)
       
def main():

 # Write code here
 N,H=input().split()
 hc=list(map(int,input().split()))
 N=int(N)
 road=[]
 start_road=[]
 end_road=[]
 for i in range(N-1):
    road.append(list(map(int,input().split()))) 
    start_road.append(road[i][0])
    end_road.append(road[i][1])
 H=int(H)
 #dis=[[0]*(H-1) for i in range(H-1)]
 dis=[]
 for i in range(len(hc)-1):   
     for j in range(i+1,len(hc)):
        r=findanotherhc(hc[i],hc[j],start_road,end_road,0)
        if(r==0):
            r=findanotherhc(hc[i],hc[j],list(reversed(start_road)),list(reversed(end_road)),0)
        if(r==0):
            r=findanotherhc(hc[i],hc[j],end_road,start_road,0)
        if(r==0):
            r=findanotherhc(hc[i],hc[j],list(reversed(end_road)),list(reversed(start_road)),0)
        if(r==0):
            r=findanotherhc(hc[j],hc[i],start_road,end_road,0) 
        if(r==0):
            r=findanotherhc(hc[j],hc[i],list(reversed(start_road)),list(reversed(end_road)),0)
        if(r==0):
            r=findanotherhc(hc[j],hc[i],end_road,start_road,0)
        if(r==0):
            r=findanotherhc(hc[j],hc[i],list(reversed(end_road)),list(reversed(start_road)),0)
        dis.append(r)

 hcc=list(combinations(hc,2))
 #print(hcc)
 
 sh=sum(hc)
 m=[]
 for i in range(len(hcc)):
     k=sum(hcc[i])
     m.append(dis[i])
     s1=set(hcc[i])
     for j in range(len(hcc)):
         if(i==j):
             continue
         s2=set(hcc[j])
         if(s1.intersection(s2)!=set()):
             continue
         s1=s1.union(s2)
         k+=sum(hcc[j])
         if (k>sh):
             m[i]=0
             break
         elif (k<=sh):
            m[i]+=dis[j]
         if k==sh:
             break
 #print(m)
 print(max(m))
main()

def allpaths(s,hc,path,dist,fdpath):
    if(path[s-1][hc-1]==1):
        dist+=1
        return dist
    p1=[]
    for i in range(len(path[0])):
        k=path[s-1][i]
        if (k==1):
            dist+=1
            fdpath.append(s)
            return allpaths(i+1,hc,path,dist,fdpath)
        p1.append(dist)
        dist=0
    return max(p1)

def allpaths(s,hc,path,dist):
    p1=[] 
    for i in range(len(path[0])):
        k=path[s-1][i]
        if (k==1):
            fdpath=[]
            dist=findanotherhc(i+1,hc,path,0,fdpath)
            if(dist==None):
                fdpath=[]
                dist=findanotherhc(hc,i+1,path,0,fdpath)
            p1.append(dist)
            dist=0
    print(p1)
    return max(p1)

8 4
2 4 5 6
1 2
1 7
1 6
2 8
3 1
3 4
5 3
Ans:6

8 4
2 4 5 8
1 2
1 7
1 6
2 8
3 1
3 4
5 3
Ans:7

8 4
5 7 8 6
1 2
1 7
1 6
2 8
3 1
3 4
5 3
Ans:6

10 6
2 4 6 8 9 10
1 2
1 7
1 6
2 8
3 1
3 4
5 3
5 9
5 10
Ans:12

10 6
4 7 6 8 9 10
1 2
1 7
1 6
2 8
3 1
3 4
5 3
5 9
5 10
Ans:12

8 8
2 4 5 6 7 8 1 3
1 2
1 7
1 6
2 8
3 1
3 4
5 3
Ans:10

8 4
6 2 4 5
1 2
1 7
1 6
2 8
3 1
3 4
5 3

checked for odd hideout city pairs, it works for 3 hideout cities now


