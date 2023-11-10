class Student:
    __slots__ = ['id', 'name', 'credits', 'gpa']
    def __init__(self, id="No id", name="No name", credits=0, gpa=0):
        self.id = id
        self.name = name
        self.credits = credits
        self.gpa = gpa

def print_student(student):
    print(student.id, student.name,student.credits, student.gpa)

def main():
    student_1 = Student(1234, "Pam")
    student_2 = Student(2000, "Jerry")

    student_1.credits = 15
    student_1.gpa = 4.0
    student_2.credits = 12
    # student_2.gpa = 3.5

    print_student(student_1)
    print_student(student_2)

if __name__ == "__main__":
    main()