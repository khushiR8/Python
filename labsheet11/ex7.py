def compress_string(s):
    if not s.isalnum():
        return 'Wrong input'
    compressed=''
    while s: 
        char=s[0]
        char_count=s.count(char)
        compressed += char+ str(char_count)
        s=s.replace(char,'')
    return compressed

