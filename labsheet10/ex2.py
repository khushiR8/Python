def CountUp (n):
    if n==0:
        return 1
    else:
        CountUp (n-1)
        print(n, end='')
  
x=4
count=CountUp(x)
print(count)  