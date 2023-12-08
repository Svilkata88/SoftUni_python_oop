from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    def __init__(self):
        super().__init__(protection=90, price=25.0)

    def increase_price(self):
        new_price = self.price * 1.1
        self.price = new_price

