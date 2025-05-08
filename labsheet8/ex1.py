#create file
#append file
#write headers
#input data,calculate square
#append data to a formatted string ie line using \t
#use \n to make new data appear on a new line  


file=open('square.txt','w')
x=file.write('Number\tSquare\n')
n=int(input('Enter a number :'))

while n!= 0 :
    square=n**2
    x=file.write(str(n)+'\t'+str(square) +'\n')
    n=int(input('Enter a number :'))
file.close()

print()
file=open('square.txt','r')
y=file.read()
print(y)
file.close()

#using exceptions
# try:
#     file=open('square.txt','w')
#     file.write('Number\tSquare\n')
#     n=int(input('enter a number:'))
#     try:
#         while n!=0:
#             square=n**2
#             file.write(str(n)+'\t'+str(square+'\n'))
#             n=int(input('enter a number:'))
#     except ValueError:
#         print('input a number')
        
#     file=open('square.txt','r')
#     x=file.read()
#     print(x)
#     file.close()
# except Exception as e:
#     print(e)