class Item:
    def __init__(self,c,d,q,b,s):
        self.c=c
        self.d=d
        self.q=q
        self.b=b
        self.s=s
    
    def display_data(self):
        print(f'Item code is {self.c}')
        print(f'Item description is {self.d}')
        print(f'Quantity in stock is {self.q}')
        print(f'Buying price is {self.b}')
        print(f'Selling price is {self.s}')
    
    def calculate_profit(self):
        return self.s - self.b
    
def main():
    product1 = Item('C001','Apple',50,5,9)
    print('Item details:')
    product1.display_data()
    print(product1.calculate_profit())
main()
    
        