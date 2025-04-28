myDictionary={
"Maldives":"Malé", "Sri-Lanka":"Colombo", "Mauritius":"Port Louis", "Seychelles":"Victoria",
"Madagascar":"Antananarivo", "Reunion":"Saint-Denis",
"Comoros":"Moroni", "Djiibouti":"Djibouti City",
"Rodrigues":"Port-Mathurin"}

#c=input("enter name of country:")
#print(myDictionary.get(c,"wrong input"))
print(myDictionary.get(input("Enter Name of Country : ")," is not in the IndianOcean"))
