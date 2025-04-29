stack=[]
stack.append(10)
stack.append(20)
stack.append(30)



for i in reversed(stack):
    print(i)

if len(stack) !=0:
    stack.pop()
else: 
    print("stack is empty")
    
if len(stack) !=0:
    print("top element:",stack[-1]) 
else:
    print("stack is empty")   