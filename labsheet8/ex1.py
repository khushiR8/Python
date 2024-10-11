#create file
#append file
#write headers
#input data,calculate square
#append data to a formatted string ie line using \t
#use \n to make new data appear on a new line

y=open('square.txt','x')
y=open('square.txt','a')
y.write('Number\tSquare\n')
data=int(input('enter a number:'))

while data !=0:
    square = data ** 2
    line=str(data)+'\t'+str(square)
    y.write(str(line)+ '\n')
    data=int(input('enter a number:'))
    
y.close()    