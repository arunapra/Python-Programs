if __name__ == '__main__':
    N = int(input())
    ls=[]
    for i in range(N):
        com,*num=input().split()
        numb=list(map(int,num))
        if com=="insert":
            ls.insert(numb[0],numb[1])
        elif com=="print":
            print(ls)
        elif com=="remove":
            ls.remove(numb[0])
        elif com=="append":
            ls.append(numb[0])
        elif com=="sort":
            ls.sort()
        elif com=="pop":
            ls.pop()
        elif com=="reverse":
            ls.reverse()
