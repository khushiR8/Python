#Write a program that allows a user to input a line of text and displays the
#number of words in the text and the number of vowels in the text.

list=[]
num_vowels=0

for i in range(1,6):
  text=str(input('enter a text:'))
  list.append(text)
  
print(list)  
print(len(list))

for char in text: #goes through each letter
    if char in text:
        num_vowels += 1

print(f'number of vowels:{num_vowels}')        
    