class Student:
    id = 'No id'
    name = 'Student'
    credits = 0
    gpa = 0.0

def print_student(student):
    print(student.id, student.name,student.credits, student.gpa)

def main():
    student_1 = Student()
    student_2 = Student()

    student_1.id = "1234"
    student_1.name = "Pam"
    student_1.credits = 14
    student_1.gpa = 4.0

    student_2.id = "2000"
    student_2.name = "Jerry"

    print_student(student_1)
    print_student(student_2)

if __name__ == "__main__":
    main()