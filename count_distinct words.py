# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
if __name__ == '__main__':
    n=int(input())
    st_dict=OrderedDict()
    for i in range(n):
        sr=input()
        if st_dict.get(sr):
            st_dict[sr]=st_dict[sr]+1
        else:
            st_dict[sr]=1
    print(len(st_dict))
    print(*st_dict.values())
        
