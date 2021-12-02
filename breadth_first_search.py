#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    # Write your code here
    out=[]
    dc=[]
    for i in range(len(edges)):
        if(edges[i][0]==s):
            dc.append(edges[i][1])
    if(s!=1):
        out.append(-1)       
    for i in range(len(edges)):
        if(edges[i][0]==s):
            out.append(6)
        elif (edges[i][0] in dc):
            out.append(12)
    for i in range(len(edges),n-1):
        out.append(-1)
    return out
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
