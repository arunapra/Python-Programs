#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    c=matrix
    l=[]
    ind=[]
    for i in range(len(matrix)):
        l.append(max(matrix[i]))
        ind.append(matrix[i].index(l[i]))
    n=len(matrix)//2
    for i in range(len(matrix)):
        if(ind[i]>=n):
            c[i].reverse()
    print(c)
    ind=[]
    tp=[]
    for i in range(len(c[0])):
        tp=[k[i] for k in c]
        l=max(tp)
        ind.append(tp.index(l))
    for i in range(len(c[0])):
        if(ind[i]>=n):
            print(c[::][i].reverse())
    tot=0
    for i in range(n):
        for j in range(n):
            tot=tot+c[i][j]
    print(c)
    return tot
                    
            
        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        #fptr.write(str(result) + '\n')
        print(result)

    #fptr.close()

