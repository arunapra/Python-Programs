import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        if(root!=None):
            print(root.data,end=" ")
        while(root!=None):
            if root.left!=None:
                print(root.left.data,end=" ")
            if root.right!=None:
                rrght=root.right
                print(root.right.data,end=" ")
            root1=root
            root=root.left
            if(root!=None):
                if (root.left==None) and (root.right==None):
                    root=root1.right
                    if root==None:
                        root=rrght
                    
            

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
