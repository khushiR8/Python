mylist=[0,1,2,3,4,5,6]
print(mylist)
print('List has',len(mylist), 'items')
mylist.append(7)
print(mylist)

for i in range(len(mylist)):
    print(mylist[i]*mylist[i])