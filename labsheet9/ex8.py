import math

def area_Circle(radius):
    area=math.pi*(radius**2)
    return area

def main():
    radius=float(input('enter radius:'))
    area=area_Circle(radius)
    print(area)
    
main()    
    