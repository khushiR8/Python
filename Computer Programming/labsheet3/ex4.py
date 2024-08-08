#ex4

d1=float(input("enter d1:"))
d2=float(input("enter d2:"))
d3=float(input("enter d3:"))
s1=float(input("enter s1:"))
s2=float(input("enter s2:"))
s3=float(input("enter s3:"))

TotalDistance = d1+d2+d3
print("total distance is:",TotalDistance)

TotalSpeed = s1+s2+s3
TimeTaken = float(TotalDistance/TotalSpeed)
Avgspeed = float(TotalDistance/TimeTaken)

print("total distance is:",TotalDistance)
print("timetaken is:",TimeTaken)
print("average speed is:",Avgspeed)