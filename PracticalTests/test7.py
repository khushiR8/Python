alphlist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
import random
newcharacterlist=[]
numberlistforfile=[]
file=open(r"C:\Users\beeda\Projects\github.com\khushiR8\Python\PracticalTests\text.txt", 'r')

linefromfile=file.readlines()
for line in linefromfile:
    numberlist=[]
    characterlist=[]
    for word in line.split():
        for letter in word:
            characterlist.append(letter)
            number=random.randint(1,100)
            numberlist.append(number)
            numberlistforfile.append(number)
            numberlistforfile.append(",")
        characterlist.append(" ")
        number=random.randint(1,100)
        numberlist.append(number)
        numberlistforfile.append(number)
        numberlistforfile.append(",")
    numberlistforfile.append("\n")
    for i in range (len(characterlist)):
        placeshift=numberlist[i]%26
        character=characterlist[i]
        newcharacter=alphlist[alphlist.index(character)+placeshift]
        newcharacterlist.append(newcharacter)
    newcharacterlist.append("\n")
file2=open(r"C:\Users\beeda\Projects\github.com\khushiR8\Python\PracticalTests\text2.txt", 'w')    
for i in range(len(newcharacterlist)):
    file2.write(newcharacterlist[i])
file3=open(r"C:\Users\beeda\Projects\github.com\khushiR8\Python\PracticalTests\text2.txt", 'w')
for i in range(len(numberlistforfile)):
    file3.write(str(numberlistforfile[i]))

    