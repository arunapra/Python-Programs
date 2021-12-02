#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    neg=0
    pos=0
    z=0
    for i in range(len(arr)):
        if arr[i]==0:
            z+=1
        elif arr[i]>0:
            pos+=1
        else:
            neg+=1
    print(round(pos/len(arr),6))
    print(round(neg/len(arr),6))
    print(round(z/len(arr),6))
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
