L=[64,25,12,22,11]
i=0
while i < len(L) - 1 :
    smallest=i
    j = i + 1
    while j < len(L) :
        if L[j] < L[smallest]:
            smallest=j
        j+=1
    L[i],L[smallest] = L[smallest],L[i]
    i+=1
print("sorted list:", L)    