#Modify the program you wrote for Question 1 so that the list is being
#populated with user input data.

list=[]

for i in range(1,6):
    user_input=int(input('enter a number:'))
    list.append(user_input)
    
for i in list:
    print(i,end=" ")    