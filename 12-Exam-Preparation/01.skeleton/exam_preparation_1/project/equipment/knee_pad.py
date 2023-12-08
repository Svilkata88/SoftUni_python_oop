from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    def __init__(self):
        super().__init__(protection=120, price=15.0)

    def increase_price(self):
        new_price = self.price * 1.2
        self.price = new_price

