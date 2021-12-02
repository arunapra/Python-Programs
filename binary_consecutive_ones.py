#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    b=bin(n)
    c1=[]
    j=0
    c1.append(0)
    for i in range(2,len(b)):
        if b[i]=='1':
            c1[j]+=1
        else:
            j=j+1
            c1.append(0)
    ls=list(reversed(sorted(c1)))
    print(ls[0])
