from project.computer_types.computer import Computer


class Laptop(Computer):
    PROCESSORS_AVAILABLE = {'AMD Ryzen 9 5950X': 900, 'Intel Core i9-11900H': 1050, 'Apple M1 Pro': 1200}
    RAM_VALID_Types = [2, 4, 8, 16, 32, 64]
    MAX_RAM = 64

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.PROCESSORS_AVAILABLE:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")
        if ram not in self.RAM_VALID_Types or ram > self.MAX_RAM:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price = self.PROCESSORS_AVAILABLE[processor] + (self.ram_price(ram))
        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."
