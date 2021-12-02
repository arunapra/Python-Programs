import sys

class Solution:
    # Write your code here
    def __init__(self):
        self.stack=[]
        self.queue=[]
        
    def pushCharacter(self,st):
        self.stack.append(st)
    
    def enqueueCharacter(self,st):
        self.queue.append(st)
    
    def popCharacter(self):
        l=len(self.stack)
        ch=self.stack[l-1]
        self.stack.pop(l-1)
        return ch
    
    def dequeueCharacter(self):
        ch=self.queue[0]
        self.queue.pop(0)
        return ch
        

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")

