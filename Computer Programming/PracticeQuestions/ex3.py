#Write a C++ program to input two binary numbers. The program should then
#add the two binary numbers and display their sum (for example, if the first binary
#number is 1010 and the second binary number is 0011, the sum of the two binary
#numbers should be 1101).

s=0

b1=input('enter a binary number :')
b2=input('enter a second binary number :')

s=bin(int(b1,2) + int(b2,2))  #base 2

print(f'Sum of binary numbers {b1} and {b2} :{s[2:]}') #{s[2:]} means starting from index 2
