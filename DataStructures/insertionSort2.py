L=[10,3,6,2,8]
i=1
while i<len(L):
    insertpt=i
    item=L.pop(i)
    j=i-1
    while j >= 0:
        if L[j]>item:
            insertpt=j
        else:
            break
        j-=1
    L.insert(insertpt,item)
    i+=1
print(L)