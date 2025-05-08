n=int(input('enter number of entries:'))
d={}
for i in range(n):
    try:
        o,e=input().split()
        d[e]=o
    except ValueError:
        print('')
        continue
    
while True:
    try:
        e_line=input().strip()
        if e_line:
            d_line=[]
            for x in e_line.split():
                if x in d:
                    d_line.append(d[x])
                else:
                    d_line.append('*'*len(x))
            print(' '.join(d_line))
    except ValueError:
        break
    
    