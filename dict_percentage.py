if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks=[]
    marks=student_marks.get(query_name)
    total=0
    for i in range(len(marks)):
        total+=marks[i]
    average=total/len(marks)
    print(format(average,".2f"))
