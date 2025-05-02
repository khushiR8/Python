
breakfast='egg'
print(breakfast.upper())
print(breakfast.lower())

if breakfast.startswith('eg'):
    print('egg start with eg',)
else:
    print('egg does not start with eg')
    
repeated = breakfast * 6
print(repeated)

txt = 'I like bananas'
txt = txt.replace('bananas','apples')
print(txt)