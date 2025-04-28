listIslands = ["Maldives", "Sri-Lanka", "Mauritius", "Seychelles", "Madagascar", "Reunion", "Comoros", "Djiibouti", "Rodrigues"]
listCapitals = ["Malé", "Colombo", "Port Louis", "Victoria", "Antananarivo", "Saint-Denis", "Moroni", "Djibouti City", "Port-Mathurin"]

myDictionary={}
for i,c in zip(listIslands, listCapitals):
    myDictionary.update({i:c})
C=input("Enter Name of Country :")
print(myDictionary.get(C," is not in the Indian Ocean"))

for i,c in listIslands.items():
    print("Island is ",i,"and capital is ",c)