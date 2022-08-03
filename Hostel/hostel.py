class Hostel:
    """This class is about details of hostels
        It has student_name,student_id,room_number attributes
        and infostudents method.It is parent class of two child class:
        BoysHostel and GirlsHostel"""
    def __init__(self,student_name,student_id,room_number):
        self.student_name=student_name
        self.student_id=student_id
        self.room_num=room_number
    def infoStudents(self):
        return f"student name : {self.student_name},student id:{self.student_id},room number:{self.room_num}"