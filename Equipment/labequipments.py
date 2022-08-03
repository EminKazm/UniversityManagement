from Equipment.equipments import Equipments
class LabEquipments(Equipments):
    """This class is the child class of Equipment and
     it contains the details of all the equipment needed for the lab.It has equipment name,count attributes.
      It has composition relantionships between Lab class"""
    def __init__(self,equipment_id,equipment_name,count,price,is_broken):
        super().__init__(equipment_id,price,is_broken)
        self.equipment_name=equipment_name
        self.count=count
