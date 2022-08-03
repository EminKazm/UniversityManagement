from department import Department
from Equipment.classroom import Classroom
class UniversityManagement:
    """This class is about details of university
        It has name,adress,contact,ranking,is_open attributes
        and isOpen,uniDetails methods
        It has composition relationships between Departmen class and Classroom class"""
    def __init__(self, name, adress, contact, ranking, is_open, departmentName, staffcount, studentscount, classId, floor, count_student,
                    is_full):
        self.name = name
        self.adress = adress
        self.contact = contact
        self.ranking = ranking
        self.is_open=is_open
        self.department=Department(departmentName,staffcount,studentscount)
        self.classroom=Classroom(classId,floor,count_student,is_full)
    def isOpen(self):
        if self.is_open:
            print("University is open")
        else:
            print("University is closed")
    def uniDetails(self):
        return f"University name:{self.name},University adress:{self.adress},contact number:{self.contact},ranking:{self.ranking}"""
