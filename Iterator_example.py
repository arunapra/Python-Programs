class ArrayList:
    def __init__(self,number_list):
        self.numbers = number_list

    def __iter__(self):
        self.pos = 0
        return self

    def __next__(self):
        if(self.pos<len(self.numbers)):
            self.pos+=1
            return self.numbers[self.pos-1]
        else:
            raise StopIteration
        
array_obj = ArrayList([1,2,3])
it = iter(array_obj)
print(next(it))
print(next(it))
print(next(it))
try:
    print(next(it))

except StopIteration as err:
    print(err)

for i in array_obj:
    print(i)
