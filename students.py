class Student:
    pass

def main():
    student_1 = Student()
    student_2 = Student()

    student_1.id = "1234"
    student_1.name = "Pam"
    student_1.credits = "14"
    student_1.gpa = "4.0"

    student_2.id = "2000"
    student_2.name = "Jerry"
    student_2.credits = "10"
    student_2.gpa = "3.5"

    print(student_1.id, student_1.name,student_1.credits, student_1.gpa, student_2.id, student_2.name,student_2.credits, student_2.gpa)

if __name__ == "__main__":
    main()