#Write a python program  that writes out the prime factorization of an integer. n = int(input("Enter an integer: "))

n=int(input('enter an integer :'))
factors = []

# Check for number of 2s in n
while n % 2 == 0:
    factors.append(2)
    n = n // 2

# Check for odd factors from 3 onwards
i = 3
while i * i <= n:
    while n % i == 0:
        factors.append(i)
        n = n // i
    i += 2

# If n is still greater than 2, then it must be prime
if n > 2:
    factors.append(n)

print(f"Prime factorization: {factors}")
