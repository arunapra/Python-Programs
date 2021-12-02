class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        s=k=0
        for i in range(len(A)-1,-1,-1):
            s=s+A[i]*(10**k)
            k=k+1
        s=s+1
        print(s)
        res=[]
        while(s>0):
            res.append(s%10)
            s=s//10
        res.reverse()
        return res

A=list(map(int,input().split()))
b=Solution()
result=b.plusOne(A)
print(result)
