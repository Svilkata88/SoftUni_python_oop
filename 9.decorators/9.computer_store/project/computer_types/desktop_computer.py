from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    PROCESSORS_AVAILABLE = {'AMD Ryzen 7 5700G': 500, 'Intel Core i5-12600K': 600, 'Apple M1 Max': 1800}
    RAM_VALID_Types = [2, 4, 8, 16, 32, 64, 128]
    MAX_RAM = 128

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.PROCESSORS_AVAILABLE:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        if ram not in self.RAM_VALID_Types or ram > self.MAX_RAM:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price = self.PROCESSORS_AVAILABLE[processor] + (self.ram_price(ram))
        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."
