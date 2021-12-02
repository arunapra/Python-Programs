''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
from itertools import combinations

def findanotherhc(s,hc,pv,path,dist):
    if(path[s-1][hc-1]==1):
        dist+=1
        return dist
    for i in range(len(path[0])):
        if(i!=(pv-1)):
            k=path[s-1][i]
        else:
            k=0
        if(k==1):
            dist+=1
            return findanotherhc(i+1,hc,s,path,dist)

def findanotherhcr(s,hc,pv,path,dist):
    if(path[s-1][hc-1]==1):
        dist+=1
        return dist
    for i in range(len(path[0])-1,-1,-1):
        if(i!=(pv-1)):
            k=path[s-1][i]
        else:
            k=0
        if(k==1):
            dist+=1
            return findanotherhcr(i+1,hc,s,path,dist)
                    
def main():

 # Write code here
 N,H=input().split()
 hc=list(map(int,input().split()))
 N=int(N)
 road=[]
 hc.sort()
 for i in range(N-1):
    road.append(list(map(int,input().split()))) 
 H=int(H)
 path=[[0]*(N) for i in range(N)]
 for i in range(N-1):
     s=road[i][0]
     e=road[i][1]
     path[s-1][e-1]=1
     path[e-1][s-1]=1
 
 dis=[]
 for i in range(len(hc)-1):   
     for j in range(i+1,len(hc)):
        r=findanotherhc(hc[i],hc[j],0,path,0)
        if(r==None):
            r=findanotherhc(hc[j],hc[i],0,path,0)
        if(r==None):
            r=findanotherhcr(hc[i],hc[j],0,path,0)
        if(r==None):
            r=findanotherhcr(hc[j],hc[i],0,path,0)
        dis.append(r)
 #print(dis)
 hcc=list(combinations(hc,2))
 
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
