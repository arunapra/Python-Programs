T = int(input())
for i in range(1,T+1):
    ls =list(map(int, input().split()))
    N = ls[0]
    D = ls[1]
    C = ls[2]
    M = ls[3]
    S = input()
    flag=True
    if ('D' in S):
        for c in S:
            if (c=='C'):
                if(C!=0):
                    C-=1
                else:
                    flag=False
                    break
            elif (c=='D'):
                if(D!=0):
                    D-=1
                    C+=M
                else:
                    flag=False
                    break
    if(flag):
        print(f"Case #{i}: YES")
    else:
        print(f"Case #{i}: NO")
