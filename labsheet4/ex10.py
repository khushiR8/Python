
n = int(input('Enter n: '))
LineNo = 1 
while LineNo <= n:
    i = 1
    while i <= LineNo:
        print(i,end='\t' ) #puts space in between
        i += 1
    print('\n') #Changes lines
    LineNo += 1
