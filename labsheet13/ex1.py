class Item:
    def __init__(self, code, desc, quantity, ubp, usp):
        self.code = code
        self.desc = desc
        self.quantity = quantity
        self.ubp = ubp
        self.usp = usp

    def display_data(self):
        print(f"Item Code: {self.code}")
        print(f"Description: {self.desc}")
        print(f"Quantity in Stock: {self.quantity}")
        print(f"Unit Buying Price: {self.ubp}")
        print(f"Unit Selling Price: {self.usp}")

    def calculate_profit(self):
        return self.usp - self.ubp

# Example usage:
def main():
    item1 = Item("A123", "Milk 1L", 50, 20.0, 25.0)
    
    print("Item Details:")
    item1.display_data()
    
    print(f"\nProfit per unit: {item1.calculate_profit()}")
main()

def main():
    code=input('enter item code:')
    desc=input('enter desc:')
    quantity=int(input('enter quantity:'))
    ubp=float(input('enter ubp:'))
    usp=float(input('enter usp:'))
    
    #create product1 using entered data
    product1=Item(code,desc,quantity,ubp,usp)
    
    print('Item details:') 
    product1.display_data()
    
    profit=product1.calculate_profit()
    print(f'profit per unit:{profit}')
main()    
