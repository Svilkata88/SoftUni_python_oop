from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('Pesho', 'Cow', 'Muu')

    def test_init(self):
        self.assertEqual('Pesho', self.mammal.name)
        self.assertEqual('Cow', self.mammal.type)
        self.assertEqual('Muu', self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual('Pesho makes Muu', result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_info(self):
        result = self.mammal.info()
        self.assertEqual('Pesho is of type Cow', result)


if __name__ == '__main__':
    main()