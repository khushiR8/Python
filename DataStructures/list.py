# Write a program which allows the user to enter the
# name of an island nation of the Indian Ocean and
# prints the capital of that island nation.

# listIslands=["Maldives", "Sri-Lanka", "Mauritius", "Seychelles", "Madagascar", "Reunion", "Comoros", "Djiibouti", "Rodrigues"]
# listCapitals=["Malé", "Colombo","Port Louis", "Victoria", "Antananarivo", "Saint-Denis", "Moroni", "Djibouti City",
# "Port-Mathurin"]
# C=input("Enter Name of Country:")
# i=listIslands.index(C) #Note: Index returns none if element is not found in list
# if i!=None:
#     print(listCapitals[i])
# else:
#     print(C+"is not in the Indian Ocean")

# better version
listIslands = ["Maldives", "Sri-Lanka", "Mauritius", "Seychelles", "Madagascar", "Reunion", "Comoros", "Djiibouti", "Rodrigues"]
listCapitals = ["Malé", "Colombo", "Port Louis", "Victoria", "Antananarivo", "Saint-Denis", "Moroni", "Djibouti City", "Port-Mathurin"]

print(listIslands)
C = input("Enter Name of Country: ")
found = False

for i in range(len(listIslands)):
    if listIslands[i].lower() == C.lower():  # Case-insensitive comparison
        print("Capital:", listCapitals[i])
        found = True
        break

if not found:
    print(C + " is not in the Indian Ocean")
