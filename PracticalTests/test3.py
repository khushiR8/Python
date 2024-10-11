
lowercase_count = [0]*26
uppercase_count = [0]*26

with open('alphabet.txt', 'r') as file:
    text = file.read()
    for char in text:
        if char.islower():
            lowercase_count[ord(char) - ord('a')] += 1
        elif char.isupper():
            uppercase_count[ord(char) - ord('A')] += 1

print("\n Total lowercase letters:")
for i in range(26):
    print(f"{chr(i + ord('a'))}: {lowercase_count[i]}")

print("\n Total Uppercase letters:")
for i in range(26):
    print(f"{chr(i + ord('A'))}: {uppercase_count[i]}")
