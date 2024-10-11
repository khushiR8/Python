
import random 
listNum=[0,0,0,0,0,0,0,0,0,0]
for i in range (100):
    num=random.randint(0,99)
    listNum[num//10]+=1

histoNum=[]
for i in range(10):
    l=[]
    for j in range(10):
        l.append(0)
    histoNum.append(l)

for i in range (len(listNum)):
    for j in range (0,listNum[i]//10+1):
        histoNum[9-j][i]=(j+1)*10
    histoNum[9-j][i]=listNum[i]%10

for i in range(10):
    for j in range(10):
        print(histoNum[i][j],"\t\t",end="")
    print()
for i in  range(len(listNum)):
    print(listNum[i],"\t\t",end="")
print()
