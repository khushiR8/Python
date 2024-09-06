i=1
s=0
count=0

while count <= 50:
    if i % 2 == 0:
       s+=i
       count+=1
    i+=1
  
print(f'Sum of even number :{s}')   