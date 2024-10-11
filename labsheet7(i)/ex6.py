list_id=[]
list_marks=[]    
num=int(input('enter number of students:'))
for i in range(num):
    id=int(input('enter id of students:'))
    while (id < 700 or id > 799):
       id=int(input('enter id of students:'))
    marks = float(input('enter marks of students :'))
    while (marks < 0 or marks > 100):
        marks=float(input('enter marks of students :'))
    list_id.append(id)
    list_marks.append(marks)
    
index_of_min = 0
index_of_max = 0
min=list_marks[0]
max=list_marks[0]

for i in range (len(list_marks)):
    if list_marks[i] < min :
      min=list_marks[i]  
      index_of_min=i     
        
    if list_marks[i]>max :
       max=list_marks[i]   
       index_of_max=i
       
print('student with id '+ str(list_id[index_of_min]) +'scored min marks of '+ str(min))   
print('student with id '+ str(list_id[index_of_max]) +'scored max marks of '+ str(max))    
       