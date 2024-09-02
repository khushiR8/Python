
s_id=[]
s_mark=[]

for i in range(1,6):
    s_id_n = int(input('enter sidn in the range 701-799 :'))
    if (s_id_n >= 701) and (s_id_n <= 799):
        print(f'correct sidn :{s_id_n}')
    else:
        print(f'incorrect sidn:{s_id_n}')
    s_id.append(s_id_n)

print(s_id)            

for j in range(1,6):
    mark=int(input('enter mark of student'))
    if (mark >= 0) and (mark <= 100):
        print(f'correct mark:{mark}')
    else:
        print(f'incorrect mark:{mark}')
    s_mark.append(mark)

s_mark.sort()
print(s_mark)
print(f'lowest mark :{s_mark[0]}')
print(f'highest mark :{s_mark[-1]}')
    