import math

def area_Circle(radius):
    area=math.pi*(radius**2)
    return area

radius=float(input('enter radius:'))
area=area_Circle(radius)
print(area)