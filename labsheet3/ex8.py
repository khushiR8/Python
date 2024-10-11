#ex8

distance=float(input("Enter distance in miles:"))
miles_per_gallon=float(input("Enter miles per gallon of the car:"))
cost_per_gallon=float(input("Enter cost of gallon:"))

gallons_needed=distance/miles_per_gallon
total_cost=gallons_needed*cost_per_gallon

print("Number of gallons needed:",gallons_needed)
print("Cost of trip:",total_cost)
                      