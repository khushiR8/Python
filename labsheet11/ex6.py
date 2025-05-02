
text='Data Science is fun and exciting'
v="aeiouAEIOU"
count=0
for char in text:
    if char in v:
        count +=1
print(count)

if text.startswith('Data') and text.endswith('exciting'):
    print('text starts with Data and ends with exciting')

    