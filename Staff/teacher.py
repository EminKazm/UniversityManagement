from Staff.staff import Staff
from Staff.salary import Salary
class Teacher(Staff):
    """It has inheritance relationships with Staff and composition with Salary class
        It has is_salary attribute and receive_salary,total_salary methods"""

    def __init__(self, name, age, pay, bonus):
        super().__init__(name,age)

        self.salary = Salary(pay, bonus)
    def receive_salary(self,is_salary):
        if is_salary==True:
            return "This month teacher recieves salary"
        else:
            return "Teacher hasnt received salary yet."

    def total_salary(self):
        return self.salary.annual_salary()

