squares = []  
for i in range(1,11):     
    squares.append(i * i)    
print(squares)

students = [100,90,80,70,60,50,40,30,0]

passed_students = list(filter(lambda x: x >= 60, students))
passed_students = [i for i in students if i >= 60]