class Mylist():
    def __init__(self,dimension):
        self.l=[0 for i in range(dimension)]
    
    def __getitem__(self,idx):
        return self.l[idx-1]

    def __setitem__(self,idx,data):
        self.l[idx-1]=data

m1=Mylist(5)
m1[1]=50
m1[2]=100
x=m1[1]
print(x)
for i in m1:
    print(i)