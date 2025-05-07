list=['a','b','b','a']
# list=['a','b','c','d']
newlist=list[::-1]

if list == newlist:
    print('symmetric')
else: 
    print('not symmetric')
    
# print(f'list before : {list}')
# print(f'list after : {newlist}')