queue=[]
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)

#queue before removing item
for item in queue:
    print(item)

if len(queue) !=0 :
    removed=queue.pop(0)
    print("item removed : ",removed)
else:
    print("queue is empty")

#queue after removing item
for item in queue:
    print(item)
    
if len(queue) !=0:
    print("front item is :", queue[0])
else:
    print("queue is empty")

queue.clear()
for item in queue:
    print(item)