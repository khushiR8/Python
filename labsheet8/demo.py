#opening files


#f=open('c:/Users/beeda/OneDrive/Desktop/CS/Computer Programming/labsheet8/demo.txt','a')
#f=open('demo.txt','a')
#print(f.read())

#f.close()

file=open('demo.txt','w')
for i in range(4):
    s=str(input('enter a sentence :'))
    x=file.write(s + '\n')  #'\n' inputs on a new line
    print(x)
file.close()

file=open('demo.txt','r')
y=file.read()
print(y)
file.close()

file=open('demo.txt','r')
for line in file:
    print('[' + line.strip() + ']')
file.close()