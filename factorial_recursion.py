#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n!=1:
        return n*factorial(n-1)
    else:
        return 1

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    #result=1
    result = factorial(n)

    #fptr.write(str(result) + '\n')

    #fptr.close()
    print(result)
