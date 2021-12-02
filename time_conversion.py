#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if (s.find('AM')!=-1):
        if(s[0:2]=="12"):
            ts="00"+s[2:8:]
        else:
            ts=s[0:8:]
    else:
        if(s[0:2]=="12"):
            ts=s[0:8:]
        else:
            t=int(s[0:2])+12
            ts=str(t)+s[2:8:]
    return ts
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
