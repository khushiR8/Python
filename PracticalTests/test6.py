class product:
    def __init__(self,c,n,p,e,q):
        self.code=c
        self.name=n
        self.price=p
        self.e_date=e
        self.qty=q
    def display(self):
        print(self.code, self.name, self.price, self.e_date, self.qty)
stockDictionary={} #empty dictionary
f=open("item.txt","r") #open file
s=f.readline() #read first line
while(s!=""): #reads lines until the end of the file
    l=s.strip().split() #.strip() removes leading whitespace, .split() splits the line into a list of words using spaces or tabs.
    if len(l) == 5: #makes sure the line has exactly 5 values
        stockDictionary[l[0]]=product(l[0],l[1],l[2],l[3],l[4]) #l[0] is used as the product code
    s=f.readline()
barcode=input("Enter code:")
if barcode in stockDictionary: #search for item
    stockDictionary.get(barcode).display() #if found, calls the .display() method 
else:
    print("Not Found")
    
    
