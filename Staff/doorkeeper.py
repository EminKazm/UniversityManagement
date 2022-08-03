from Staff.staff import Staff
from Staff.salary import Salary
class DoorKeeper(Staff):
    """It has inheritance relationships with Staff and composition with Salary class and
        It has is_salary attribute and receive_salary,total_salary methods"""
    def __init__(self,name,age,pay,bonus):
        super().__init__(name,age)

        self._obj_salary = Salary(pay, bonus)

    def receive_salary(self, is_salary):
        if is_salary == True:
            print("Teacher recieves salary")
        else:
            print("Teacher dont has any money.")

    def total_salary(self):
        return self._obj_salary.annual_salary()
