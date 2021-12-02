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
    newt=""
    if(s[0:2]=="12"):
        if(s[-1:-3:-1]=="MA"):
            newt="00"+s[2:len(s)-2]
        else:
            newt=s[0:len(s)-2]
    else:
        if(s[-1:-3:-1]=="MA"):
            newt=s[0:len(s)-2]
        else:
            ho=int(s[0:2])+12
            newt=str(ho)+s[2:len(s)-2]
    return newt
        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
