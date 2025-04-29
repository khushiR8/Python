def InsertionSort(L):
    for i in range(1,len(L)):
        insertpt=i
        item=L.pop(i)
        for j in range(i-1,-1,-1):
            if L[j] > item:
                insertpt=j
            else:
                break
        L.insert(insertpt,item)
    return L
        
x=[10,3,2,7,8]
sortedlist=InsertionSort(x)
print(sortedlist)






        