def word():
    text = input('Enter a text: ')  # Get user input
    text_list = list(text)           # Convert the input text to a list of characters
    text_list.reverse()              # Reverse the list
    return text_list                 # Return the reversed list

# Call the function
reversed_text = word()              # Store the reversed list
print("Reversed text as a list:", reversed_text)  # Print the result
