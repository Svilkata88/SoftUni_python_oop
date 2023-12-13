from project.trip import Trip
from unittest import TestCase, main


class TestTrip(TestCase):
    def setUp(self) -> None:
        self.trip1 = Trip(100.0, 2, True)
        self.trip2 = Trip(100.0, 1, False)

    def test_init(self):
        self.assertEqual(100, self.trip1.budget)
        self.assertEqual(2, self.trip1.travelers)
        self.assertEqual(True, self.trip1.is_family)
        self.assertEqual({}, self.trip1.booked_destinations_paid_amounts)

    def test_travelers_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.trip1.travelers = 0
        self.assertEqual('At least one traveler is required!', str(ex.exception))

    def test_is_family_setter(self):
        self.assertFalse(self.trip2.is_family)
        self.trip2.is_family = True
        self.assertFalse(self.trip2.is_family)

    def test_book_a_trip_not_existing_destination(self):
        self.trip1.book_a_trip('Mars')
        self.assertEqual('This destination is not in our offers, please choose a new one!',
                         self.trip1.book_a_trip('Mars'))

    def test_book_a_trip_successfully_family_true(self):
        self.trip1.budget = 11400
        self.assertEqual(f'Successfully booked destination Australia! '
                         f'Your budget left is 1140.00', self.trip1.book_a_trip('Australia'))
        self.assertIn('Australia', self.trip1.booked_destinations_paid_amounts)
        self.assertEqual(10260.0, self.trip1.booked_destinations_paid_amounts['Australia'])

    def test_book_a_trip_successfully_family_false(self):
        self.trip1.budget = 11400
        self.trip1.is_family = False
        self.assertEqual(f'Successfully booked destination Australia! '
                         f'Your budget left is 0.00', self.trip1.book_a_trip('Australia'))
        self.assertIn('Australia', self.trip1.booked_destinations_paid_amounts)
        self.assertEqual(11400.0, self.trip1.booked_destinations_paid_amounts['Australia'])

    def test_book_a_trip_with_not_enough_budget(self):
        self.assertEqual('Your budget is not enough!', self.trip1.book_a_trip('Australia'))

    def test_booking_status_with_no_bookings_yet(self):
        self.assertEqual(f'No bookings yet. Budget: 100.00', self.trip1.booking_status())

    def test_booking_status_with_1_booking(self):
        self.trip1.budget = 10260
        self.trip1.book_a_trip('Australia')
        self.assertEqual(f"""Booked Destination: Australia
Paid Amount: 10260.00\n"""
                         """Number of Travelers: 2
Budget Left: 0.00""", self.trip1.booking_status())

    def test_booking_status_with_2_bookings(self):
        self.trip1.budget = 50000
        self.trip1.book_a_trip('Bulgaria')
        self.trip1.book_a_trip('Australia')
        self.assertEqual('Booked Destination: Australia\n'
                         'Paid Amount: 10260.00\n'
                         'Booked Destination: Bulgaria\n'
                         'Paid Amount: 900.00\n'
                         'Number of Travelers: 2\n'
                         'Budget Left: 38840.00'
                         , self.trip1.booking_status())



if __name__ == '__main__':
    main()
