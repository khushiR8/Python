#taking the name of the 3 files

first = input("Enter the name of the first file: ")
second = input("Enter the name of the second file: ")
merge = input("Enter the name of the merging file: ")

first = first + '.txt'
second = second + '.txt'
merge = merge + '.txt'
#appending data in file1
a = open(first,'a')
data = input("Enter data to input in file1: ")
while data != '0':
    a.write(data)
    a.write('\n')
    data = input("Enter data to input in file (or 0 to stop): ")

#appending data in file2
b = open(second,'a')
data = input("Enter data to input in file2: ")
while data != '0':
    b.write(data)
    b.write('\n')
    data = input("Enter data to input in file (or 0 to stop): ")

#reading files
a = open(first,'r')
b = open(second,'r')

#merging the 2 files 
c = open(merge,'w')

#appending data from file1 to target
for line in a:
    c.write(line)

#appending data from file2 to target
for line in b:
    c.write(line)

c = open(merge,'r')
for line in c:
    print(line)

a.close()
b.close()
c.close()