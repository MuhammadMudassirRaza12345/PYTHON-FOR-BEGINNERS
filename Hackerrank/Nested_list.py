#Given the names and grades for each student in a class of N  students, store them in a nested list and
#print the name(s) of any student(s) having the second lowest grade.

#Note: If there are multiple students with the second lowest grade, order their names alphabetically and
# print each name on a new line.

# if __name__ == '__main__':
#     students = []
#     scores=[]
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         students+=[[name, score]]
#         scores+=[score]
   
#     b=sorted(list(set(scores)))[1]
#     # d=b[1]
     
#     for a,c in sorted(students):
#         if c==b:
#             print(a)


#second way

if __name__ == '__main__':
    students = []
    scores=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students+=[[name, score]]
        scores+=[score]
   
    b=sorted(list(set(scores))) 
    d=b[1]
     
    for a,c in sorted(students):
        if c==d:
            print(a)
    