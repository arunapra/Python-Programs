#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    # Write your code here
    pairs=0
    for i in range(len(arr)):
        d1=arr[i]
        for j in range(i+1,len(arr)):
            if(i!=j):
                if(arr[j]>d1):
                    di=arr[j]-d1
                else:
                    di=d1-arr[j]
                if (di==k):
                    pairs+=1
    print(pairs)
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
