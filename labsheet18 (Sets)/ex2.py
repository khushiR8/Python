x=set()
y=set()
while True:
    barcode=input('enter barcode for item by employe1:')
    if barcode=='':
        break
    if barcode in x:
        print('already scanned')
    else:
        x.add(barcode)

while True:
    barcode=input('enter barcode for item by employee2:')
    if barcode=='':
        break
    if barcode in y:
        print('already scanned')
    else:
        y.add(barcode)

totalx=len(x)
totaly=len(y)

scanneditems=x.union(y)
totalscanneditems=len(scanneditems)

print(f'total items scanned by employee1: {x}')
print(f'total items scanned by employee2: {y}')
print(f'unique items in warehouse: {totalscanneditems}')