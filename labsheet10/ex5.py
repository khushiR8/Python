def digit(n):
    if n<10:
        return 1
    else:
        return 1 + digit(n//10)

x=100
checkdigit=digit(x)
print(digit)