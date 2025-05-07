name=[]
maths=[]
phy=[]

n=int(input('enter number of students:'))
for i in range(n):
    studentname=str(input(f'enter name of student {i+1}:'))
    name.append(studentname)
    markinmaths=float(input(f'enter marks in maths:'))
    maths.append(markinmaths)
    markinphy=float(input(f'enter marks in physics:'))
    phy.append(markinphy)

print(name)
x=str(input('enter student to search:'))
if x in name:
    index=name.index(x)
    print(f'{x} scored {maths[index]} in maths and {phy[index]} in physics')
else:
    print(f'student not found')
    
highest=0
top=''
for i in range(n):
    total=maths[i]+phy[i]
    if total>highest:
        highest=total
        top=name[i]
print(f'top student is {top} has a total of {highest} marks')
   