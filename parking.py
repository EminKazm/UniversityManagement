class Park:
    """This class contains the details of the parking area in a college
        It has car_name,drivername,vehiclenumber attributes
        and detailsVehicle method """
    def __init__(self,car_name,drivername,vehiclenumber):
        self.car_name=car_name
        self.driver_name=drivername
        self.vehicle_num=vehiclenumber

    def detailsVehicle(self):
        return f"car name:{self.car_name},name of driver:{self.driver_name},vehicle number:{self.vehicle_num}"




