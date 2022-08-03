from Equipment.equipments import Equipments
class ClassEquipments(Equipments):
    """This class is the base class of two child classes – Lab Equipments and Class Equipments.
    it has table_count chair_count board_count attributes"""
    def __init__(self,equipment_id,price,is_broken,table_count, chair_count, board_count):
        super().__init__(equipment_id,price,is_broken)
        self.table=table_count
        self.chair=chair_count
        self.board=board_count
