student=[]
maths=[]
phy=[]

for i in range(1,3):
    name=str(input('enter name of student:'))
    math_mk=float(input('enter marks in maths:'))
    phy_mk=float(input('enter marks in physics:'))
    student.append(name)
    maths.append(math_mk)
    phy.append(phy_mk)

for i in range(1,3):    
    if name in student:
     index=student.index(name)
     print(f'{name} marks')
     print(f'Maths: {maths[index]}')
     print(f'Phy: {phy[index]}')
     
max=0
top=''
for i in student:
    total=maths[i] + phy[i]
    if total > max:
        max=total
        top=student[i]
print(f'Top student is {top} with total marks of {max}')          

    
    
    