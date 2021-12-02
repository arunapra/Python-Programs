#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    ls=[]
    for i in range(4):
        for j in range(4):
            ls.append(sumf(i,j))
    return max(ls)

def sumf(i,j):
    s=0
    for k in range(i,(i+3)):
        for m in range(j,(j+3)):
            if(k==(i+1)) and ((m==j) or (m==(j+2))):
                continue
            s+=arr[k][m]
    return s
                   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
