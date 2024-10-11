mylist=[1,2,3,4,5,6]
print(mylist)
print('The list has',len(mylist),'items')
mylist.append(7)
print(mylist)
for i in range(len(mylist)):
 print(mylist[i]*mylist[i]) #multiply i by 1 e.g 2*2=4