#opening files


#f=open('c:/Users/beeda/OneDrive/Desktop/CS/Computer Programming/labsheet8/demo.txt','a')
#f=open('demo.txt','a')
#print(f.read())

#f.close()

a=open('trial.txt','x')
a=open('trial.txt','a')
a.write("hello")
a=open('trial.txt','r')
print(a.read())

a.close()
