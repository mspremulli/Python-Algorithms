import collections
numberOfStudents = int(input())

titles = input()
grades = collections.namedtuple("Grade", titles)


total = 0
for data in range(numberOfStudents):
    data = input().split()
    student = grades(data[0],data[1],data[2],data[3])
    total += int(student.MARKS)

print(total / numberOfStudents)