#input a sticker
#stop when 0 is input
#input a sticker to compare with the list of stickers

s=set()
while True:
    sticker=int(input('enter a sticker:'))
    if sticker ==0:
        break
    s.add(sticker)
print(s)
while True:
    check=int(input('enter a sticker to check:'))
    if check==0:
        break
    if check in s:
        print(f'already has card {check}')
    else:
        print(f'does not have it')
    s.add(check)
print(s)