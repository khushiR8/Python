#Write a program which allows the user to enter two integers 'a' and 'b' your program should
# then display all the multiples of 'a' which lie between o and 'b'.
# Note that your program should ensure that 'a' is less than 'b' through proper validation.

while True:
    a=int(input('enter value of a:'))
    b=int(input('enter value of b:'))
    
    if a < b:
      break   
    else:
        print(f'Invalid input a should be < than b')
        
print(f'Multiples of {a} between 0 and {b}')
for i in range (a,b+1,a):
    print(i)        
       