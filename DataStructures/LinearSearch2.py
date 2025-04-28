list=[10,20,30,40,50]
n=int(input("Enter a number to search:"))
found=False

for i in range(len(list)):
    if list[i] == n:
        print(f"Element found at index {i}")
        break
if not found:
    print(f"Element not found in the list")
    
