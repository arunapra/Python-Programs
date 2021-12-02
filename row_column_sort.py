#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    ng=[]
    nl=[]
    for i in range(len(grid)):
        nl=list(grid[i])
        nl.sort()
        ns="".join(nl)
        ng.append(ns)
    count=0
    for i in range(len(ng[0])):
        s=""
        for j in range(len(ng)):
            s+=ng[j][i]
        cl=list(s)
        sl=sorted(cl)
        if cl==sl:
            count+=1
        else:
            return "NO"
    if count==len(ng[0]):
        return "YES"
    else:
        return "NO"
        
        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        print(result)

        #fptr.write(result + '\n')

    #fptr.close()
