import random

list=[]
for i in range (12):
    x=[]
    for j in range(12):
        x.append(0)
    list.append(x)

for i in range(1,12):
    for j in range(1,12):
        y=random.randint(0,1)
        list[i][j]=y
        
for i in range(1,12):
    for j in range(1,12):
        print(list[i][j],"",end=" ")
    print("\n") 

for i in range(5):
    for i in range(1,11):
        for j in range(1,11):
            sum=list[i][j-1]+list[i][j+1]+list[i+1][j]+list[i-1][j]+list[i-1][j-1]+list[i-1][j+1]+list[i+1][j+1]+list[i+1][j-1]
            if (list[i][j]==1 or list[i][j]==0) and (sum==0 or sum==1 or sum==2):
                list[i][j]=0
            elif list[i][j]==1 and sum>=4:
                list[i][j]=0
            elif list[i][j]==0 and sum>=3:
                list[i][j]=1 
            elif list[i][j]==1 and sum>3:
                list[i][j]=1

print('New generation')
for i in range(1,12):
    for j in range(1,12):
        print(list[i][j],"",end=" ")
    print("\n")    
                                   
                               