student_heights=input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(student_heights)
print(sum(student_heights)/len(student_heights))