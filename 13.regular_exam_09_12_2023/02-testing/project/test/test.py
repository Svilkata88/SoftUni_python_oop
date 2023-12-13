from collections import deque

from project.railway_station import  RailwayStation
from unittest import TestCase, main


class TestRailwayStation(TestCase):

    def setUp(self):
        self.railway_station = RailwayStation('Ruse')

    def test_init(self):
        self.assertEqual('Ruse', self.railway_station.name)
        self.assertEqual(deque([]), self.railway_station.arrival_trains)
        self.assertEqual(deque([]), self.railway_station.departure_trains)

    def test_name_is_valid(self):
        with self.assertRaises(ValueError) as ex:
            self.railway_station.name = 'Rus'
        self.assertEqual("Name should be more than 3 symbols!", str(ex.exception))

    def test_new_train_on_board(self):
        self.railway_station.new_arrival_on_board('train 1')
        self.assertEqual(deque(['train 1']), self.railway_station.arrival_trains)

    def test_train_has_arrived_wrong_train(self):
        self.railway_station.new_arrival_on_board('train 1')
        self.railway_station.new_arrival_on_board('train 2')
        self.assertEqual("There are other trains to arrive before train 2.",
                         self.railway_station.train_has_arrived('train 2'))

    def test_train_has_arrived_correct_train(self):
        self.railway_station.new_arrival_on_board('train 1')
        self.assertEqual(f"train 1 is on the platform and will leave in 5 minutes.",
                         self.railway_station.train_has_arrived('train 1'))
        self.assertEqual(deque(['train 1']), self.railway_station.departure_trains)

    def test_train_left_true(self):
        self.railway_station.new_arrival_on_board('train 1')
        self.railway_station.train_has_arrived('train 1')
        self.assertEqual(True, self.railway_station.train_has_left('train 1'))
        self.assertEqual(deque([]), self.railway_station.departure_trains)

    def test_train_left_false(self):
        self.railway_station.new_arrival_on_board('train 1')
        self.railway_station.new_arrival_on_board('train 2')
        self.railway_station.train_has_arrived('train 1')
        self.assertEqual(False, self.railway_station.train_has_left('train 2'))
        self.assertEqual(deque(['train 1']), self.railway_station.departure_trains)

    def test_train_left_false_departure_trains_0(self):
        self.railway_station.new_arrival_on_board('train 1')
        self.assertEqual(False, self.railway_station.train_has_left('train 2'))
        self.assertEqual(deque([]), self.railway_station.departure_trains)


if __name__ == "__main__":
    main()
