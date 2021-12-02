class ArrayList():
    def __init__(self,data):
        self.data=data
    
    def __iter__(self):
        self.pos=0
        return self
    
    def __next__(self):
        if(self.pos<len(self.data)):
            self.pos+=1
            return self.data[self.pos-1]
        else:
            raise StopIteration

a=ArrayList([1,2,3])
k=iter(a)
print(next(k))
print(next(k))
print(next(k))
print(next(k))
