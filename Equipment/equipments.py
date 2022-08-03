class Equipments:
    """This class is the base class of two child classes – Lab Equipments and Class Equipments."""
    def __init__(self,equipment_id,price,is_broken):
        self.equipment_id=equipment_id
        self.price=price

        self.is_broken=is_broken
    def infoEquipment(self):
        return f"equipment id:{self.equipment_id},price:{self.price},"
    def repair(self):
        if self.is_broken:
            print("it needs to repair")
        else:
            print("it is not broken")



