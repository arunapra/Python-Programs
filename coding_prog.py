class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def averagef(self):
        total = sum(self.marks)
        average = total/len(self.marks)
        return average

avg = []
for i in range(3):
    name = input("Enter the student name")
    marks = list(map(int, input().split()))
    ch = Student(name, marks)
    
    avg.append(ch.averagef())

print(avg)
print(sorted(avg, reverse=True))

