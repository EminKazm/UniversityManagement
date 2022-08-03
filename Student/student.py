class Student:
    """This class is about details of students
        It has studentname,gender,age attributes and
        infostudent ageofstudent methods
        It is parent class of two child class:MasterStudent and Bachelor"""
    def __init__(self,studentname,gender,age):
        self._student_name=studentname
        self._gender=gender
        self._age=age
    def infoStudent(self):
        print( f"Student name:{self._student_name},gender of student:{self._gender},Student age:{self._age}")
    def ageofstudents(self):
        try:
            self.age = int(self._age)
            if (self.age < 13):
                raise ValueError
            else:
                print("the age is valid")
        except ValueError:
            print("The age is not valid")







