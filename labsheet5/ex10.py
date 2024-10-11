capital=int(input('enter capital :'))
interest=int(input('enter interest :'))
num_yrs=0
target =2*capital

while capital < target:
    capital=interest * capital
    num_yrs +=1
print(f'capital: {capital}')
print(f'years: {num_yrs}')
