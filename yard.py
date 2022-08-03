class Yard:
    """This class is about details of yard
        It has weight,length attributes
        and setweight,getweight,setlength,getlength,area methods"""
    def __init__(self,weight,length):
        self.__weight=weight
        self.__length=length
    def setweight(self,weight):
        self.__weight=weight
    def getweight(self):
        return self.__weight
    def setlength(self,length):
        self.__length=length
    def getlength(self):
        return self.__length
    def area(self):
        return self.__length*self.__weight





