# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
strin,siz=input().split()
r=int(siz)
per_list = list(permutations(strin,r))
for i in range(len(per_list)):
    s=""
    for j in range(r):
        s=s+str(per_list[i][j])
    print(s)
