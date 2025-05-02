while True:
    testmark=int(input("Enter test mark:"))
    if testmark < 0 or testmark > 30:
        print('invalid mark entered ,should be between 0 and 30')
    else:
        break


while True:
    exammark=int(input("Enter exam mark:"))
    if exammark < 0 or exammark > 70:
        print('invalid mark entered, should be between 0 and 70')
    else:
        break
    
totalmark = testmark + exammark
print(totalmark)

if totalmark < 40:
    print('F')
elif totalmark>=40 and totalmark<50:
    print('D')
elif totalmark>=50 and totalmark<60:
    print('C')
elif totalmark>=60 and totalmark<70:
    print('B')
elif totalmark>=70 and totalmark<80:
    print('A')
elif totalmark>=80 and totalmark<100:
    print('A+')