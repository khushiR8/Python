# Since tuples are immutable, we have to convert it to a list 
# and then add or remove an element 
# and convert it back to a tuple

myTuple=("Red", "Blue", "Yellow", "Green")
print(myTuple)
myList=list(myTuple)
myList.append("Black")
myList.remove("Red")
print(myList)
myTuple=tuple(myList)
print(myTuple)