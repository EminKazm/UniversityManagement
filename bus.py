class Bus:
    """This is about details of university bus
       It has busid,driver_name,totalseats,passenger attributes
       and busdetails,seatsavailability methods"""
    def __init__(self,busid,driver_name,totalseats,passenger):
        self.busid=busid
        self.driver=driver_name
        self.totalseats=totalseats
        self.passenger=passenger
    def busDetails(self):
        return f"bus id:{self.busid},driver name:{self.driver},total seats of bus:{self.totalseats}"
    def seatsavailability(self):
        if self.totalseats>=self.passenger:
            print( "You can sit")
        else:
            print( "You must stand on your feet")

