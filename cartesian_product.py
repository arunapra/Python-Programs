# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
list1= list(map(int, input().rstrip().split()))
list2= list(map(int, input().rstrip().split()))
#print(list(product(list1,list2)))
cart_list=list(product(list1,list2))
for i in range(len(cart_list)):
    print(cart_list[i],end=" ")
