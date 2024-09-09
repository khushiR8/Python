#Write a program which reverses the digits.For example, if n is 927, it would return 729. Apply the function in a
#program that asks the user to enter 10 numbers and reverses them.

numbers = []
reversed_numbers = []

# Get 10 numbers from the user
for i in range(3):
    n = int(input(f"Enter number {i + 1}: "))
    numbers.append(n)
    
    # Reverse the number without using a function
    reversed_num = 0
    while n > 0:
        digit = n % 10  # Get the last digit
        reversed_num = reversed_num * 10 + digit  # Build the reversed number
        n = n // 10  # Remove the last digit
    
    reversed_numbers.append(reversed_num)

# Output the reversed numbers
print("\nOriginal numbers and their reversals:")
for i in range(3):
    print(f"Original: {numbers[i]}, Reversed: {reversed_numbers[i]}")
