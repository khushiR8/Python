#descending use <
#ascending use >
def BubbleSort(L):
    for i in range(len(L)-1):
        swap=False
        for j in range(len(L)-i-1):
            if L[j]<L[j+1]:
                L[j+1],L[j]=L[j],L[j+1]
                swap=True
        if swap == False:
            break
    return L
   
x=[2342,45,12,5,6897,78]
sortedbubble=BubbleSort(x)
print(sortedbubble)