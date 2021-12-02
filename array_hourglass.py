#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    sumt=[] 
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(4):
        for j in range(4):
            times=0
            sumh=0
            while(times<3):
                k=j
                if times==0:
                    count=0
                    while(count<3):
                        sumh+=(arr[i][k])
                        k+=1
                        count+=1
                elif times==1: 
                    sumh+=arr[i+1][k+1]  
                else:
                    count=0
                    while(count<3):
                        sumh+=(arr[i+2][k])
                        k+=1
                        count+=1
                times+=1
            sumt.append(sumh)
    print(max(sumt))
