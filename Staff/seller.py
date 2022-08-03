from Staff.staff import Staff
from Staff.salary import Salary
class Seller(Staff):
    """It has inheritance relationships with Staff and composition with Salary class and
        also composition relantionships with Canteen class
            It has is_salary attribute and receive_salary,total_salary methods"""
    def __init__(self, seller_id,name, age,pay,bonus):
        super().__init__(name,age)
        self._seller_id=seller_id
        self.salary = Salary(pay, bonus)
    def set_id(self,seller_id):
        self._seller_id=seller_id
    def get_id(self):
        return self._seller_id



    def receive_salary(self, is_salary):
        if is_salary == True:
            print("Seller recieves salary")
        else:
            print("Seller hasnt receive salary yet.")

    def total_salary(self):
        return self.salary.annual_salary()

