class Classroom:
    """This class is about details of classroom
       it has classId ,floor,count_student,department attributes
       and isfull infoclassroom methods
       it has relationship compositon with university management class"""
    def __init__(self,classId,floor,count_student,is_full):
        self.class_id=classId
        self.floor=floor
        self.count_student=count_student
        self.is_full=is_full

    def infoClassroom(self):
        return f"class id:{self.class_id},floor:{self.floor},count:{self.count_student}"
    def isFull(self):
        if self.is_full:
            print("classroom is full")
        else:
            print("classroom is not full")


