def SelectionSort(L):
    i=0
    while i<len(L)-1:
        smallest=i
        j=i+1
        while j < len(L):
            if L[j] < L[smallest]:
                smallest=j
            j+=1
        L[i],L[smallest]=L[smallest],L[i]
        i+=1
    return L

x=[64,25,12,34,11]
sortedlist=SelectionSort(x)
print(sortedlist)