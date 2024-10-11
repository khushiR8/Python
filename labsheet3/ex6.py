#ex6,area of cylinder=2πrh+2πr2

radius=float(input("Enter radius of cylinder:"))
height=float(input("Enter height of cylinder:"))

area = (2*3.142*radius*height) + (2*3.142*radius**2)

print("Area of cylinder is:",area)