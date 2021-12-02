#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    
    flag="YES"
    if(len(s)%2!=0):
        flag="NO"
        return flag
    open_b=['{','[','(']
    close_b=['}',']',')']
    cu1=s.count(open_b[0])
    cu2=s.count(close_b[0])
    if (cu1!=cu2):
        flag="NO"
        return flag
    sq1=s.count(open_b[1])
    sq2=s.count(close_b[1])
    if (sq1!=sq2):
        flag="NO"
        return flag
    p1=s.count(open_b[2])
    p2=s.count(close_b[2])
    if (p1!=p2):
        flag="NO"
        return flag  
    c=[]  
    for i in range(len(s)):
        if(s[i] in open_b):
            c.append(s[i])
        elif(s[i] in close_b) and len(c)>0:
            if open_b.index(c[-1])==close_b.index(s[i]):
                c.pop()
            else:
                flag="NO"
                return flag 
    return flag 
        
        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)
        print(result)
        #fptr.write(result + '\n')

    #fptr.close()
