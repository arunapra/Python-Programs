# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
if __name__ == '__main__':
    n=int(input())
    store=OrderedDict()
    for i in range(n):
        *name,price = input().split()
        name=" ".join(name)
        if name in list(store.keys()):
            store[name]=store[name]+int(price)
        else:
            store[name]=int(price)
    for name,price in store.items():
        print(name,price)
