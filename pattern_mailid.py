#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    firstName=[]
    emailID=[]
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName.append(firstNameEmailID[0])

        emailID.append(firstNameEmailID[1])
   
    gmaillist=[]
    for i in range(N):
        if emailID[i].find("@gmail.com")!=-1:
            gmaillist.append(firstName[i])
    gmaillist.sort()
    for i in range(len(gmaillist)):
        print(gmaillist[i])
