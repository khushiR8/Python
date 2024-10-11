a=open('square.txt','r')
sum=0
largest=0
smallest=99999
count=0
a.readline() #read and discard the first line which contain headers

for line in a: #loop through each remaining line in the file
    count+=1   #increment the count for each line processed
    new=line.split('\t') #split the line into a list using tab
    num=int(new[0]) #convert the first element of the split line to an integer
   
    sum+=num
    
    if num > largest:
        largest=num
    
    if num < smallest:
        smallest=num
    
average=int(sum/count)     
        
print("Sum      ", sum)   
print("Average  ", average)     
print("Largest  ", largest)     
print("Smallest ", smallest)    