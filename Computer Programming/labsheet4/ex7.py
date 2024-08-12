#ex7

human_years = float(input("Enter human years :"))

if human_years <= 2:
    dog_years = human_years*10.5
    print("Dog years :",dog_years)
else:
    dog_years =  (2*10.5) + ((human_years -2)*4)
    print("Dog years :",dog_years)