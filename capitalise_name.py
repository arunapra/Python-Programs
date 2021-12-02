#!/bin/python3

s=input()
sp=0
news=""
for i in range(len(s)):
    if i==0 and (s[i].isalpha()):
        news+=s[i].upper()
    elif s[i].isspace():
        sp=1
        news+=s[i]
    elif sp==1 and s[i].isalpha():
        news+=s[i].upper()
        sp=0
    else:
        news+=s[i]
        sp=0
print(news)
