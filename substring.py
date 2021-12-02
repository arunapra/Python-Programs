def merge_the_tools(string, k):
    # your code goes here
    i=0
    while(i<len(string)):
        m=""
        for j in range(0,k):
            if m.find(string[i+j])==-1:
                m=m+string[i+j]
        print(m)
        i=i+j+1

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
