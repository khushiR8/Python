list_id=[]
list_mark=[]
n=int(input('enter the number of students :'))
for i in range(n):
    while True:
        id=int(input('Enter id of students :'))
        if id < 701 or id > 799:
            print('Id should be betweem 701 and 799')
        else:
            break
        
    while True:
        mark=float(input('Enter mark of students :'))
        if mark < 0 and mark > 100:
            print('Mark should be between 0 and 100')
        else:
            break
    list_id.append(id)
    list_mark.append(mark)
           
print(list_id)
print(list_mark)

index_of_min=0
index_of_max=0
min=list_mark[0]
max=list_mark[0]

for i in range (len(list_mark)):
    if list_mark[i]<min:
        min=list_mark[i]
        index_of_min=i
        
    if list_mark[i]>max:
        max=list_mark[i]
        index_of_max=i

print('student with id '+ str(list_id[index_of_min]) +'scored min marks of '+ str(min))   
print('student with id '+ str(list_id[index_of_max]) +'scored max marks of '+ str(max))    
       
