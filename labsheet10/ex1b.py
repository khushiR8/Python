def add(n):
    if n==1 :
        return 2
    else:
        return 2*n + add(n-1)
x=5
sum=add(x)
print(sum)