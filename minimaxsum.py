#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    ls=[]
    for i in range(len(arr)):
        tot=0
        for j in range(len(arr)):
            if i!=j:
                tot=tot+arr[j]
        ls.append(tot)
    ls.sort()
    print(ls[0],ls[-1])

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
