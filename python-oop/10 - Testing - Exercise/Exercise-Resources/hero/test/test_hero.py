import unittest

from project.hero import Hero

DEFAULT_USERNAME = 'Test'
DEFAULT_LEVEL = 1
DEFAULT_HEALTH = 100
DEFAULT_DAMAGE = 10
HERO_REPRESENTATION = "Hero Test: 1 lvl\n" \
    "Health: 100\n" \
    "Damage: 10\n"


class HeroTests(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero(username=DEFAULT_USERNAME, level=DEFAULT_LEVEL,
                         health=DEFAULT_HEALTH, damage=DEFAULT_DAMAGE)

    def test_hero_ok_init(self):
        self.assertEqual(DEFAULT_USERNAME, self.hero.username)
        self.assertEqual(DEFAULT_LEVEL, self.hero.level)
        self.assertEqual(DEFAULT_HEALTH, self.hero.health)
        self.assertEqual(DEFAULT_DAMAGE, self.hero.damage)

    def test_hero_battling_himself_raises(self):
        h = Hero('Test', 2, 50, 30)
        with self.assertRaises(Exception):
            self.hero.battle(h)

    def test_hero_battle_when_hero_health_negative_raises(self):
        self.hero.health = -5
        h = Hero('Test1', 2, 50, 30)
        with self.assertRaises(ValueError):
            self.hero.battle(h)

    def test_hero_battle_when_hero_health_zero_raises(self):
        self.hero.health = 0
        h = Hero('Test1', 2, 50, 30)
        with self.assertRaises(ValueError):
            self.hero.battle(h)

    def test_hero_battle_when_enemy_health_negative_raises(self):
        h = Hero('Test1', 2, 50, 30)
        h.health = -5
        with self.assertRaises(ValueError):
            self.hero.battle(h)

    def test_hero_battle_when_enemy_health_zero_raises(self):
        h = Hero('Test1', 2, 50, 30)
        h.health = 0
        with self.assertRaises(ValueError):
            self.hero.battle(h)

    def test_hero_battle_damage(self):
        h = Hero('Test1', 2, 50, 10)
        enemy_health = 45
        self.hero.battle(h)
        self.assertEqual(enemy_health, h.health)

    def test_hero_battle_hero_win(self):
        h = Hero('Test1', 2, 10, 2)
        rv = self.hero.battle(h)
        self.assertTrue(h.health <= 0)
        self.assertEqual('You win', rv)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(15, self.hero.damage)
        self.assertEqual(101, self.hero.health)

    def test_hero_battle_enemy_win(self):
        h = Hero('Test1', 23, 100, 200)
        rv = self.hero.battle(h)
        self.assertTrue(self.hero.health <= 0)
        self.assertEqual('You lose', rv)
        self.assertEqual(24, h.level)
        self.assertEqual(205, h.damage)
        self.assertEqual(95, h.health)

    def test_hero_battle_draw(self):
        h = Hero('Test1', 1, 2, 200)
        rv = self.hero.battle(h)
        self.assertTrue(self.hero.health <= 0)
        self.assertTrue(h.health <= 0)
        self.assertEqual('Draw', rv)

    def test_hero_str_representation(self):
        self.assertEqual(HERO_REPRESENTATION, str(self.hero))


if __name__ == "__main__":
    unittest.main()
