class Staff:
    def __init__(self,n,a,g,s):
        self.n=n
        self.a=a
        self.g=g
        self.s=s
    def display(self):
        print(f'Staff name : {self.n}')
        print(f'Staff address : {self.a}')
        print(f'Staff gender : {self.g}')
        print(f'Staff salary : {self.s}')
    def update(self,newadd,newsal):
        self.a=newadd
        self.s=newsal

def main():
    name=str(input('enter name of staff :'))
    addr=str(input('enter address of staff :'))
    gender=str(input('enter gender of staff :'))
    salary=float(input('enter salary of staff :'))
    worker1=Staff(name,addr,gender,salary)
    worker1.display()
    worker1.update('port louis',25000)
    worker1.display()
main()    
    