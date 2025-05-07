first=str(input('enter name of the first file:'))
second=str(input('enter name of the second file:'))
third=str(input('enter name of the third file:'))

first=first +'.txt'
second=second +'.txt'
third=third +'.txt'

file1=open(first,'w')
data=input('Enter data in file1:')
while data !='0':
    file1.write(data + '\n')
    data=input('Enter data in file1:')
    
file2=open(second,'w')
data=input('Enter data in file2:')
while data !='0':
    file2.write(data + '\n')
    data=input('Enter data in file2:')

file1=open(first,'r')
file2=open(second,'r')

file3=open(third,'w')
for line in file1:
    file3.write(line)
for line in file2:
    file3.write(line)
    
file3=open(third,'r')
for line in file3:
    print(line)
    
    
file1.close()
file2.close()
file3.close()