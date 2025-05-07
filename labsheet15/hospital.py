class Staff:
    def __init__(self,n,a,g,s):
        self.n=n
        self.a=a
        self.g=g
        self.s=s

    @property
    def n(self):
        return self.n
    @n.setter
    def n(self,value):
        self.n=value
    @property
    def a(self):
        return self.a
    @a.setter
    def a(self,value):
        self.a=value
    @property
    def g(self):
        return self.g
    @g.setter
    def g(self,value):
        self.g=value
    @property
    def s(self):
        return self.s
    @s.setter
    def s(self,value):
        self.s=value
        
    def monthly_income(self):
        return self.s
    
    def display_data(self):
        print(f'Name: {self.n}')
        print(f'Address: {self.a}')
        print(f'Gender: {self.g}')
        print(f'Salary: {self.s}')
    
class Doctor(Staff):
    def __init__(self,n,a,g,s,sp,fee,days):
        super().__init__(n,a,g,s)
        self.sp=sp
        self.fee=fee
        self.days=days
        
    @property
    def sp(self):
        return self.sp
    @sp.getter
    def sp(self,value):
        self.sp=value
    @property
    def fee(self):
        return self.fee
    @fee.getter
    def fee(self,value):
        self.fee=value
    @property
    def days(self):
        return self.days
    @days.setter
    def days(self,value):
        self.days=value
    
    def monthly_income(self):
        return (self.s+self.fee)*self.days
    
    def display_data(self):
        super().display_data
        print(f'Specialisation: {self.sp}')
        print(f'Daily fee: {self.fee}')
        print(f'Number of days worked: {self.days}')
        print(f'Monthly income: {self.monthly_income()}')

class Nurse(Staff):
    def __init__(self,n,a,g,s,dept,hrs,rate):
        super().__init__(n,a,g,s)
        self.dept=dept
        self.hrs=hrs
        self.rate=rate
        
    @property
    def dept(self):
        return self.dept
    @dept.setter
    def dept(self,value):
        self.dept=value
    @property
    def hrs(self):
        return self.hrs
    @hrs.setter
    def hrs(self,value):
        self.hrs=value
    @property
    def rate(self):
        return self.rate
    @rate.setter
    def rate(self,value):
        self.rate=value
    
    def monthly_income(self):
        return self.s+(self.hrs*self.rate)
    
    def display_data(self):
        super().display_data()
        print(f'Department: {self.dept}')
        print(f'Overtime hours: {self.dept}')
        print(f'Overtime rate: {self.dept}')
        print(f'Monthly income: {self.monthly_income()}')
        
def main():
    staff1 = Staff("Sam", "Port Louis", "Male", 30000)
    staff1.display_data()
    print(f"Monthly Income: {staff1.monthly_income()}")
    doctor1 = Doctor("Dr Sam", "Maurice", "Male", 50000, "Cardiology", 2000, 20)
    doctor1.display_data()
    nurse1 = Nurse("Alia", 'Reduit', "Female", 25000, "Pediatrics", 15, 200)
    nurse1.display_data()
main()

