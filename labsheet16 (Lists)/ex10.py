import math

def calcsq(L):
    count=0
    for row in L:
        for num in row:
          if num >=0:
              sqroot=math.isqrt(num)
              if sqroot*sqroot == num:
                  count+=1
    return count

List = [
    [1, 2, 3],
    [4, 5, 9],
    [7, 16, 8]
]

x=calcsq(List)
print(x)