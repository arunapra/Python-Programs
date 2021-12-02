''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
from itertools import permutations
from copy import deepcopy
def main():

 # Write code here 
 N = int(input())
 vi=[]
 for i in range(N):
     vi.append(int(input()))
 vi.insert(N//2,"st")
 ncomb = 0
 fcomb=[]
 for j in range(3,N+1):
    mstcomb=list(permutations(vi,j))
    #print(j)
    #print(mstcomb)
    for k in mstcomb:
        t_list = list(k)
        if("st" in t_list):
            c1=c2=0
            for m in t_list:
                if(m!="st"):
                    c1+=m
                else:
                    c2=c1
                    c1=0
            if(c1==c2):
                fcomb.append(t_list)
                ncomb+=1
 #print(fcomb)
 cset = set(fcomb[0])
 print(cset)
 for y in fcomb:
     ind=y.index('st')
     del y[ind]
 
 ecomb=deepcopy(fcomb)
 for b in range(len(fcomb)):
     fw=sorted(fcomb[b])
     for y in range(len(fcomb)):
         if(y!=b):
            cw=sorted(fcomb[y])
            if (fw==cw):
                if(y<len(ecomb)):
                    del ecomb[y]
 print(len(ecomb))


main()
