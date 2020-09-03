"""N = int(input("Enter number of students: "))
dic = {}
markList = []
for i in range (0,N):
    k = input("Enter name of student: ")
    for j in range (3):
            marks = (input("Enter Marks: "))
            markList.append(marks)
    dic.update({k:markList})

print(dic)"""

sum1 =0
x = int(input("Enter number of elements: "))
for i in range (x):
    a = int(input("Enter element {}: ".format(i+1)))
    sum1 += a

print(sum1)
