list=[0,1,2,3,4,5,6]
print(list)
print('The list has',str(len(list)),'items')
list.append(7)
print(list)
for i in range(len(list)):
    print(str(list[i]*list[i]))
