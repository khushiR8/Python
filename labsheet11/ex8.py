
string=str(input('enter a string :'))
if string.isnumeric() :
    print('correct string')
    number=int(string)
    double=number*2
    print(double)
    
else:
    print('string cannot contain characters hence:')
    reversed=string[::-1]
    print(reversed)
