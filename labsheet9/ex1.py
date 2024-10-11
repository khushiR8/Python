def student_marks():
    marks=[]
    for i in range(4):
        mark=float(input('enter mark :'))
        marks.append(mark)
    return marks

def calc_avg(marks):
    return sum(marks)/4
        
def get_grade(average):
    if average > 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'        

def process_students():
    for student in range(1, 21):
        print(f"\nEntering marks for Student {student}:")
        marks = student_marks()
        average = calc_avg(marks)
        grade = get_grade(average)
        print(f"Student {student}: Average = {average:.2f}, Grade = {grade}")

process_students()    