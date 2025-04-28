#Indexing
def LinearSearch(k, L):
    i = 0
    for i in range(len(L)):
        if L[i] == k:
            return i
    return -1 #means not found


# #iterate
# def LinearSearch(k,L):
#     i=0
#     for val in L:
#         if val==k:
#          return i
#         i+=1
#     return -1

my_list = [10, 20, 30, 40, 50]
key = 30
x = LinearSearch(key, my_list)
if x != -1:
    print(f"Element found at index {x}")
else:
    print("Element not found")

