# Enter your code here. Read input from STDIN. Print output to STDOUT
date1=input().split()
date2=input().split()
d1=int(date1[0])
m1=int(date1[1])
y1=int(date1[2])
d2=int(date2[0])
m2=int(date2[1])
y2=int(date2[2])
if y1<y2:
    fine=0
elif y1>y2:
    fine=10000
elif m1>m2:
    fine=500*(m1-m2)
elif d1>d2:
    fine=15*(d1-d2)
else:
    fine=0
print(fine)
