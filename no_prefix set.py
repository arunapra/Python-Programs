#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    # Write your code here
    k=[]
    for i in range(len(words)):
        for j in range(len(words)):
            if(i!=j):
                if(words[j].find(words[i])==0):
                    k.append(j)
    
    if(len(k)>0):
        k.sort()
        print('BAD SET')
        print(words[k[0]])
        return
    print("GOOD SET")
                

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
