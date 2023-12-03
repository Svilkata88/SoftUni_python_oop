from typing import List
from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    VALID_COMPUTER_TYPES = {"Desktop Computer": DesktopComputer, "Laptop": Laptop}

    def __init__(self):
        self.warehouse: List[Computer] = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.VALID_COMPUTER_TYPES:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        computer = self.VALID_COMPUTER_TYPES[type_computer](manufacturer, model)
        result = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return result

    def sell_computer(self, client_budget_price: int, wanted_processor: str, wanted_ram: int):
        searched_computer = next((c for c in self.warehouse if c.processor == wanted_processor and c.ram >= wanted_ram),
                                 None)
        if not searched_computer or client_budget_price < searched_computer.price:
            raise Exception("Sorry, we don't have a computer for you.")
        self.warehouse.remove(searched_computer)
        profit = client_budget_price - searched_computer.price
        self.profits += profit
        return f'{searched_computer} sold for {client_budget_price}$.'
