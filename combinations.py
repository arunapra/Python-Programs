# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
strin,siz=input().split()
r=int(siz)
for k in range(1,r+1):
    per_list = list(combinations(sorted(strin),k))
    for i in range(len(per_list)):
        s=""
        for j in range(k):
            s=s+str(per_list[i][j])
        print(s)
