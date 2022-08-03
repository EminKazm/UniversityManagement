class Staff:
    """This class is about details of Staff
    It has name,age attributes and staffDetails,ageofstaffs
    It is parent class of child classes:seller,teacher,librarian,doorkeeper"""
    def __init__(self,name,age):
        self.name=name
        self._age=age
    def staffDetails(self):
        return f"name:{self.name} age:{self._age}"
    def ageofstaffs(self):
        try:
            self.age = int(self._age)
            if (self.age < 17):
                raise ValueError
            else:
                print("age is valid")
        except ValueError:
            print("age is invalid")





