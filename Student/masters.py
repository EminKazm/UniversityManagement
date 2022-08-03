from Student.student import Student
class MasterStudent(Student):
    """This class is about details of master students
        It has inheritance relationships with students"""
    def __init__(self, studentname, gender,age):
        Student.__init__(self, studentname, gender,age)
        print("Information about master students")