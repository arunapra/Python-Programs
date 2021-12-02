from functools import reduce

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    t=0
    ls=[]
    new_ls=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                ls.append([i,j,k])
                t+=1
    print(ls)
    new_ls=[ls[q] for q in range(t) if (reduce(lambda acc,num:acc+num,ls[q],0)!=n)]
    print(new_ls)
