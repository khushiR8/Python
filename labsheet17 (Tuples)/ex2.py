# t=((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# avg=0
# total=0
# count=0
# avglist=[]
# for row in range(len(t)):
#     for col in range(len(t[row])):
#         total+=t[row][col]
#         count+=1
#     avg=total/count
#     avglist.append(avg)
# print(avglist)

t=((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
avg=0
total=0
count=0
avglist=[]
for col in range(len(t)):
    for row in range(len(t[col])):
        total+=t[row][col]
        count+=1
    avg=total/count
    avglist.append(avg)
print(avglist)