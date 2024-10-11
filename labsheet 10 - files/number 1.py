y = open('Squares.txt','x')
y = open('Squares.txt','a')
y.write('Number\tSquare\n')
data = int(input("Input a data (or 0 to stop): "))
while data != 0:
    square = data ** 2 
    line = str(data) + '\t'+ str(square)
    y.write(str(line)+ '\n')
    data = int(input("Input a data (or 0 to stop): "))
y.close()
