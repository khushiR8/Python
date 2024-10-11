def count_words(text):
    words=text.split()
    return len(words)

def count_vowels(text):
    vowels="aeiouAEIOU"
    count=0
    for char in text:
        if char in vowels:
            count+=1
    return count

def main():
    line=input('enter a line of text :')
    word_count=count_words(line)
    vowel_count=count_vowels(line)

    print(f'Number of words :{word_count}')  
    print(f'Number of vowels :{vowel_count}')  
      
main()      