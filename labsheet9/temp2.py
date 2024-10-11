#using value returning functions

def temp(depth):
    c=10*depth+20
    f=1.8*c+32
    return c,f

calc_temp=temp(10)

print(calc_temp)