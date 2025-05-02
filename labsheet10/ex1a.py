def add(n):
    if n==0 :
        return 1
    else:
        return n+add(n-1)
    
x=8
sum=add(x)
print(sum)