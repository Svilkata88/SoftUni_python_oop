from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.car = Vehicle(6.25, 150)

    def test_init(self):
        self.assertEqual(6.25, self.car.fuel)
        self.assertEqual(150, self.car.horse_power)
        self.assertEqual(6.25, self.car.capacity)
        self.assertEqual(1.25, self.car.fuel_consumption)

    def test_drive_with_enough_fuel(self):
        self.car.drive(5)
        # fuel needed = 5 * 1.25 = 6.25 ltr.
        # fuel is equal to fuel needed in this case!
        self.assertEqual(0, self.car.fuel)

    def test_driver_fuel_less_than_fuel_needed(self):
        # fuel needed = 6 * 1.25 = 7.50 ltr.
        # fuel is less to fuel needed in this case!
        with self.assertRaises(Exception) as ex:
            self.car.drive(6)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_below_the_capacity(self):
        self.car.drive(5)
        self.car.refuel(4)
        self.assertEqual(4, self.car.fuel)

    def test_refuel_over_car_capacity(self):
        self.car.drive(5)
        with self.assertRaises(Exception) as ex:
            self.car.refuel(7)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_equal_to_car_capacity(self):
        self.car.drive(5)
        self.car.refuel(6.25)
        self.assertEqual(6.25, self.car.fuel)

    def test_str(self):
        self.assertEqual(f"The vehicle has {self.car.horse_power} horse power with {self.car.fuel} "
                         f"fuel left and {self.car.fuel_consumption} fuel consumption", self.car.__str__())


if __name__ == '__main__':
    main()


