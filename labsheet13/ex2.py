class staff:
    def __init__(self,name,addr,gender,salary):
        self._name=name
        self._addr=addr
        self._gender=gender
        self._salary=salary
    
    def display(self):
        print(f'name:{self._name}')
        print(f'addr:{self._addr}')
        print(f'gender:{self._gender}')
        print(f'salary:{self._salary}')
          
    def update(self,newaddr,newsal):
        self._addr=newaddr
        self._salary=newsal
    
def main():
    name=input('enter name:')
    addr=input('enter address:')
    gender=input('enter gender:') 
    salary=int(input('enter salary:'))
    
    worker1=staff(name,addr,gender,salary)
    
    worker1.display()
    
    worker1.update('rosebelle',40000)
    
    worker1.display()
main()    
