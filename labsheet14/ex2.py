class Staff:
    total_staff=0
    def __init__(self,n,a,g,s):
        self.n=n
        self.a=a
        self.g=g
        self.s=s
        Staff.total_staff+=1
    def display(self):
        print(f'Staff name : {self.n}')
        print(f'Staff address : {self.a}')
        print(f'Staff gender : {self.g}')
        print(f'Staff salary : {self.s}')
    def update(self,newadd,newsal):
        self.a=newadd
        self.s=newsal
    
    @staticmethod
    def calculate_annual_income(s):
        return s*12
    
    def filter_high_income_staff(self,slist,threshold):
        highincomestaff=[]
        for i in slist:
            annualincome=Staff.calculate_annual_income(i.s)
            if annualincome>threshold:
                highincomestaff.append(i)
        return highincomestaff
        
        
def main():
    list=[]
    for i in range(2):
        name=str(input('enter name of staff :'))
        addr=str(input('enter address of staff :'))
        gender=str(input('enter gender of staff :'))
        salary=float(input('enter salary of staff :'))
        worker=Staff(name,addr,gender,salary)
        list.append(worker)
        # worker1.update('port louis',25000)
    for i in list:
        print()
        i.display()
        print()
        
    threshold=float(input('Enter income threshold :'))
    highincome=worker.filter_high_income_staff(list,threshold)
    for i in highincome:
        print(f'{i.n} Annual income : {Staff.calculate_annual_income(i.s)}')

    print(f'Current number of items : {Staff.total_staff}')
main()    
    