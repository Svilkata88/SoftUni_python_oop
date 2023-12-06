from project.hero import Hero
from unittest import TestCase, main


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero('Test Hero', 10, 100.0, 10.0)
        self.enemy_hero = Hero('Enemy hero', 10, 120.0, 10.0)

    def test_init(self):
        self.assertEqual('Test Hero', self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100.0, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_attributes_types(self):
        self.assertIsInstance(self.hero.username, str)
        self.assertIsInstance(self.hero.level, int)
        self.assertIsInstance(self.hero.health, float)
        self.assertIsInstance(self.hero.damage, float)

    def test_if_hero_name_is_equal_to_enemy_hero_name(self):
        self.enemy_hero.username = 'Test Hero'
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_if_hero_health_not_enough(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as error:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(error.exception))

        self.hero.health = -1
        with self.assertRaises(ValueError) as error1:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(error1.exception))

    def test_if_enemy_hero_health_not_enough(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as error1:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(error1.exception))

        self.enemy_hero.health = -1
        with self.assertRaises(ValueError) as error2:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(error2.exception))

    def test_draw(self):
        self.enemy_hero = Hero('Test Hero 1', 10, 100.0, 10.0)

        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("Draw", result)
        self.assertEqual(self.hero.damage, self.enemy_hero.damage)
        self.assertEqual(self.hero.level, self.enemy_hero.level)
        self.assertEqual(0.0, self.hero.health)

    def test_hero_wins(self):
        self.enemy_hero = Hero('Test Hero 1', 9, 100.0, 10.0)

        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("You win", result)
        self.assertEqual(15.0, self.hero.damage)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(15.0, self.hero.health)

    def test_enemy_hero_wins(self):
        self.enemy_hero = Hero('Test Hero 1', 10, 110.0, 20.0)

        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("You lose", result)
        self.assertEqual(25.0, self.enemy_hero.damage)
        self.assertEqual(11, self.enemy_hero.level)
        self.assertEqual(15.0, self.enemy_hero.health)

    def test_str(self):
        expected = f'Hero {self.hero.username}: {self.hero.level} lvl\n' \
                   f'Health: {self.hero.health}\n' \
                   f'Damage: {self.hero.damage}\n'
        self.assertEqual(expected, str(self.hero))


if __name__ == '__main__':
    main()
