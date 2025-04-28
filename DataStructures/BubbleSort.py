def BubbleSort(L):
    for i in range(len(L)-1):
        for j in range(len(L)-i-1):
            if L[j]>L[j+1]:
                L[j+1],L[j]=L[j],L[j+1]
    return L

x=[23,56,12,3245,54,5]
sortedbubble=BubbleSort(x)
print(sortedbubble)