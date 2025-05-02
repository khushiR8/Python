class Item:
    total_items=0
    def __init__(self,c,d,q,b,s):
        self.c=c
        self.d=d
        self.q=q
        self.b=b
        self.s=s
        Item.total_items+=1
    def display_data(self):
        print(f'Item code is {self.c}')
        print(f'Item description is {self.d}')
        print(f'Quantity in stock is {self.q}')
        print(f'Buying price is {self.b}')
        print(f'Selling price is {self.s}')  
    def calculate_profit(self):
        return self.s - self.b
        
    @staticmethod
    def calculate_total_profit(q,b,s):
        return q*(s-b)       
    
def main():
    list=[]
    product1 = Item('C001','Apple',50,5,9)
    product2 = Item('C002','Banana',80,20,27)
    product3= Item('C003','Pear',100,10,18)
    list.append(product1)
    list.append(product2)
    list.append(product3) 
    for i in list:
        print('Item details:')
        print()
        i.display_data()
        print(f'Profit is : {i.calculate_profit()}')
        print()
    # for i in list:
    #     print('Item profit :')
    #     print(f'Profit is : {i.calculate_profit()}')
    print(f'Current number of items : {Item.total_items}')
main()
    
        