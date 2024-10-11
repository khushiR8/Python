#input a random (0-10)appartment in an array of 10 elements
#check position of appartment
#if noise =1 ,noisy else if noise =0 ,not noisy
#if noise > 1 ,calculate sum around 

import random
sr1=0
sr2=0
sr3=0
listApp=[0,0,0,0,0,0,0,0,0,0]
for i in range (11):
    app=random.randint(0,99)
    listApp[app//10]+=1

histoApp=[]
for i in range(11):
    l=[]
    for j in range(11):
        l.append(0)
    histoApp.append(l)

#print(listApp)
#print(histoApp)

for i in range (len(listApp)):
    for j in range (0,listApp[i]//10+1):
        if j == 0 :
            print('not noisy')
        elif j == 1:
            print('noisy')
        elif j > 1 :
            sr1 = listApp[i][j]+listApp[i][j-1]+listApp[i][j-1]   

#i i+j, i j-1, i j+1
print(sr1)
for i in range(10):
    for j in range(10):
        print(histoApp[i][j],"\t\t",end="")
    print()
for i in  range(len(listApp)):
    print(listApp[i],"\t\t",end="")
print()