#Write a program that allows the entry of an integer value n, followed by two
#sets of n integer values into lists A and B. The program should display the
#sum of corresponding values of A and B.

A=[]
B=[]
T=[]

for i in range(1,6):
    n=int(input('enter a number for A:'))
    A.append(n)
print(f'List for A :{A}') 

for i in range(1,6):
    n=int(input('enter a number for B:'))
    B.append(n)
print(f'List for B :{B}')   

T.extend(A)  #or T=A+B
T.extend(B)
print(f'List for T:{T}')  
print(f'sum of A and B :{sum(T)}') 