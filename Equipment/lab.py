from Equipment.labequipments import LabEquipments
class Lab:
    """this class is about lab
        It has composition relantionships between Labequipments class
        It has labid,name,totalequipments,isfull,totalseats attributes
        and infolab,fulllab methods"""
    def __init__(self, labID, name, totalequipments, isfull, totalseats,equipment_id, equipment_name, count,price,is_broken):
        self._lab_id=labID
        self.name=name
        self.totalequipments=totalequipments
        self.isfull=isfull
        self.totalseats=totalseats
        self.lab_equips=LabEquipments(equipment_id,equipment_name,count,price,is_broken)

    def infoLab(self):
        return f"lab id:{self._lab_id},lab name:{self.name},total equipments:{self.totalequipments},total seats:{self.totalseats},{self.lab_equips.infoEquipment()}"
    def fullLab(self):
        if self.isfull:
            print("LAB is full.")
        else:
            print("lab is not full")
