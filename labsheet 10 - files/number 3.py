a = open("Squares.txt","r")
sum = 0
largest = 0 
smallest = 9999
count = 0  
a.readline() #first line 'Number	Square'
for line in a:
    count += 1 
    new = line.split('\t')
    num = int(new[0])
    sum = sum + num
    if num > largest:
        largest = num 
    if num < smallest: 
        smallest = num

average = int(sum/count)
print("Sum      ",sum)
print("Average  ",average)
print("Largest  ",largest)
print("Smallest ",smallest)
