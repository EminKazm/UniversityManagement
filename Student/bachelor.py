from Student.student import Student
class Bachelor(Student):
    """This class is about details of bachelor students
    It has inheritance relationships with students"""
    def __init__(self, student_name, gender, age):
        super().__init__(student_name, gender, age)
        print("Information about bachelor students")