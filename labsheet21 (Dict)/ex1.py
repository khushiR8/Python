class Item:
    def __init__(self,barcode,name,price):
        self.barcode=barcode
        self.name=name
        self.price=price
    def display_details(self):
        print(f'Barcode number: {self.barcode}')
        print(f'Name: {self.name}')
        print(f'Price: {self.price}')
        
def main():
    d={}
    while True:
        print(f'\n--------Shop menu--------')
        print("1. Add item to database")
        print("2. Display all items")
        print("3. Query item by barcode")
        print("4. Exit")
        
        c=int(input('enter choice [1-4]: '))
        if c==1:
            barcode=input('enter barcode number: ')
            if barcode in d:
                print('An item with this barcode already exists')
            else:
                name=input('enter name of item:')
                try:
                    price=float(input('enter price of item:'))
                    item=Item(barcode,name,price)
                    d[barcode]=item
                    print('item added successfully')
                except ValueError:
                    print('invalid price,enter a number')
        elif c==2:
            if d:
                print(f'\n--All items in the database--')
                for item in d.values():
                    print(item.display_details())
            else:
                print('no items in the database')
        elif c==3:
            search=input('enter barcode to search: ')
            item=d.get(search)
            if item:
                print(item.display_details())
            else:
                print('no itme found with that barcode')
        elif c==4:
            print('Exit program')
            break
        else:
            print('invalid choice , enter between 1-4')
main()