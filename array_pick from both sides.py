class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        s1=0
        for i in range(B):
            s1+=A[i]
        s2=c=0
        for i in range(len(A)-1,-1,-1):
            if(c<B):
                s2+=A[i]
                c+=1
            else:
                break
        s3=c=i=0
        while(c<B):
            if(A[i]>A[len(A)-1-i]):
                s3+=A[i]
            else:
                s3+=A[len(A)-1-i]
            i+=1
            c+=1
        ls=[s1,s2,s3]
        return max(ls)
    
A=list(map(int,input().split()))
B=int(input())
b=Solution()
result=b.solve(A,B)
print(result)

