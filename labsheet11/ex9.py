text='hello my name is khushi'

try:
    char =text[10]
    print('character at index 10:', char)
except IndexError:
    print('Index error: the string is too short to access index 10')
