#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    # Write your code here
    a.sort()
    s1=[]
    s2=[]
    for i in range(len(a)):
        if i%2==0:
            s1.append(a[i])
        else:
            s2.append(a[i])
    uv=s1[0]
    for i in range(len(a)//2):
        if s1[i]==s2[i]:
            uv=s1[i+1]
    return uv
        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
