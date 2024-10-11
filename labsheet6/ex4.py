#Write a program to display all prime numbers within a 
# range, e.g start range= 25, end range = 50

prime=True
#n=int(input('enter n:'))
start=int(input('enter start of the range:'))
end=int(input('enter end of the range:'))

for i in range (start,end,1):
    if end % i ==0:
        prime=False
        print(i)
        
if prime:
    print('i is a prime number',i)
else:
    print('i is not a prime number',i)