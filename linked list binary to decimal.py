class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Solution:
    def display(self,head):
        current=head
        while current:
            print(current.data,end=" ")
            current=current.next

    def insert(self,head,data):
        self.node=Node(data)
        if(head==None):
            return self.node
        else:
            current=head
            while current.next!=None:
                current=current.next
            current.next=self.node
            return head
def bintodec(head):
    current=head
    lenl=0
    while current:
        lenl+=1
        current=current.next
    dec=0
    current=head
    for i in range((lenl-1),-1,-1):
        if current!=None:
            data=current.data
            dec+=(2**i)*data
        current=current.next
    return dec
        
    
mylist=Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head)
print()
print(bintodec(head))
