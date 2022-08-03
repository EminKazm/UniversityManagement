class Department:
    """This class is about the details of various departments in the university
        It has departmentname,staffcount,studentscount attributes
        and departDetails method
        It has composition relationship with UniversityManagement class"""
    def __init__(self,departmentName,staffcount,studentscount):
        self.depar_name=departmentName
        self.staffcount=staffcount
        self.studentscount=studentscount
    def depart_Details(self):
        print(f"department name:{self.depar_name},total staff:{self.staffcount},total students:{self.studentscount}")
