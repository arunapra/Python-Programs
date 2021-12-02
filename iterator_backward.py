class Backward():
    def __init__(self,data):
        self.data=data
        self.index=len(self.data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index==0:
            raise StopIteration
        else:
            self.index-=1
            return self.data[self.index]
            
n=Backward(eval(input()))
for i in n:
    print(i,end=" ")
