from Staff.seller import Seller

class Canteen:
    """This class is for storing Canteen details inside the school
        it has item_list,available_list,price attributes and
        display,available_items methods """

    def __init__(self,items_list, available_list,price):

        self.items_list = items_list
        self.available_list = available_list
        self.price = price
        self.seller_id=Seller("101","Nargiz",42,500,100)

    def display(self):
        return f"These are the items {self.items_list} currently available in the canteen and and " \
               f"these are the prices of items in sequence {self.price}"


    def available_items(self):
        return f"count of available items:{self.available_list} "


