file=open('square.txt','r')
y=file.readline()
print(y)

sum=0
avg=0
count=0
largest=0
smallest=99999

for line in y:
    count+=1
    new=line.split('\t')
    n=int(new[0])
    sum+=n
    if n>largest:
        largest=n
    if n<smallest:
        smallest=n
avg=int(sum/count)

print("Sum      ", sum)   
print("Average  ", avg)     
print("Largest  ", largest)     
print("Smallest ", smallest)    