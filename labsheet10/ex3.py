def checkstring(word):
    if word == '':
        return False
    if word== word[::-1]:
        print('Palindrome')
        return True
    else:
        print('Not palindrome')
        return False
    
x='wow'
check=checkstring(x)
print(check)