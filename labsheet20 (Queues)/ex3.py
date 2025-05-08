class Student:
    tokencount=1
    def __init__(self,name):
        self.name=name
        self.token=Student.tokencount
        Student.tokencount+=1
    def display_details(self):
        return f'Name: {self.name} has token number: {self.token}'

def main():
    q=[]
    while True:
        print('\n ------Library Menu------')
        print(f'1. Insert a new student')
        print(f'2. View student at the front of the queue')
        print(f'3. Delete a student from the queue')
        print(f'4. Show number of student in the queue')
        print(f'5. Exit')
        
        c=int(input('enter a choice (1,2,3,4,5): '))
        if c==1:
            n=input('enter name of student: ')
            student=Student(n)
            q.append(student)
            print(f'student added, token number: {student.token}') 
        elif c==2:
            if q:
                print(f'student at front of the queue: {q[0].display_details()}')
            else:
                print(f'queue is empty')
        elif c==3:
            if q:
                removed=q.pop(0)
                print(f'removed student: {removed.display_details()}')
            else:
                print(f'queue is empty')
        elif c==4:
            print(f'number of students: {len(q)}')
        elif c==5:
            print(f'Exiting program')
        else:
            print(f'invalid choice, enter a valid optiion')
            
main()            
                   