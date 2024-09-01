evenCount=0
oddCount=0

for i in range (1,10):
    if i % 2== 0 :
        evenCount+=1
      
    elif i % 2 !=0:
        oddCount+=1
   
print('even count is:',evenCount)        
print('odd count is:',oddCount)