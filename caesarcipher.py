#!/bin/python3

import math
import os
import random
import re
#import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    enc_s=""
    if(k==0)or(k==26):
        return s
    elif k>26:
        n=k//26
        k=k-(n*26)
    for i in s:
        if (i.isalpha()):
            if ((i.islower()) and ((ord(i)+k)>=123)) or ((i.isupper()) and ((ord(i)+k)>=91)):
                num=(ord(i)+k)-26
            else:
                num=ord(i)+k
            enc_s+=chr(num)
        else:
            enc_s+=i        
    return enc_s
        
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
