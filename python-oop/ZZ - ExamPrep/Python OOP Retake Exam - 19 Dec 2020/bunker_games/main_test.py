from project import *
import unittest


class TestItems(unittest.TestCase):
    def test_supply_raises_ValueError_when_needs_increase_goes_negative(self):
        f = FoodSupply()
        w = WaterSupply()
        message = 'Needs increase cannot be less than zero.'
        with self.assertRaises(ValueError) as fe:
            f.needs_increase -= 100
            self.assertEqual(message, str(fe))
        with self.assertRaises(ValueError) as we:
            w.needs_increase -= 100
            self.assertEqual(message, str(we))

    def test_supply_increases_survivor_needs_after_apply(self):
        f = FoodSupply()
        w = FoodSupply()
        s1 = Survivor('one', 2)
        s1.needs -= 40
        f.apply(s1)
        w.apply(s1)
        self.assertEqual(100, s1.needs)

    def test_medicine_raises_ValueError_when_health_increase_goes_negative(self):
        p = Painkiller()
        s = Salve()
        message = 'Health increase cannot be less than zero.'
        with self.assertRaises(ValueError) as pe:
            p.health_increase -= 100
            self.assertEqual(message, str(pe))
        with self.assertRaises(ValueError) as se:
            s.health_increase -= 100
            self.assertEqual(message, str(se))


class TestSurvivor(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Survivor('SurvivorName', 2)

    def test_survivor_init(self):
        self.assertEqual('SurvivorName', self.s.name)
        self.assertEqual(2, self.s.age)
        self.assertEqual(100, self.s.health)
        self.assertEqual(100, self.s.needs)

    def test_survivor_raises_ValueError_with_empty_name_or_age(self):
        wrong_name = 'Name not valid!'
        wrong_age = 'Age not valid!'
        with self.assertRaises(ValueError) as en:
            s = Survivor('', 10)
            self.assertEqual(wrong_name, str(en))
        with self.assertRaises(ValueError) as ea:
            s = Survivor('Name', -5)
            self.assertEqual(wrong_age, str(ea))

    def test_survivor_raises_ValueError_when_needs_or_health_negative(self):
        wrong_needs = 'Needs not valid!'
        wrong_health = 'Health not valid!'
        s = Survivor('Name', 10)
        with self.assertRaises(ValueError) as en:
            s.needs -= 110
            self.assertEqual(wrong_needs, str(en))
        with self.assertRaises(ValueError) as eh:
            s.health -= 110
            self.assertEqual(wrong_health, str(eh))


class TestBunker(unittest.TestCase):
    def setUp(self) -> None:
        self.s1 = Survivor('one', 2)
        self.s2 = Survivor('two', 2)

        survivors = [self.s1, self.s2]
        food = [FoodSupply(), FoodSupply(), FoodSupply(), FoodSupply()]
        water = [WaterSupply(), WaterSupply(), WaterSupply(), WaterSupply()]
        painkillers = [Painkiller(), Painkiller(), Painkiller(), Painkiller()]
        salves = [Salve(), Salve(), Salve(), Salve()]

        self.b = Bunker()

        for p in survivors:
            self.b.add_survivor(p)

        for f in food:
            self.b.add_supply(f)

        for w in water:
            self.b.add_supply(w)

        for p in painkillers:
            self.b.add_medicine(p)

        for s in salves:
            self.b.add_medicine(s)

    def test_bunker_data_is_correct_after_creation(self):
        self.assertEqual(2, len(self.b.survivors))
        self.assertEqual(4, len(self.b.food))
        self.assertEqual(4, len(self.b.water))
        self.assertEqual(4, len(self.b.painkillers))
        self.assertEqual(4, len(self.b.salves))

    def test_survivors_data_is_correct(self):

        self.assertEqual('one', self.s1.name)
        self.assertEqual('two', self.s2.name)
        self.assertEqual(2, self.s1.age)
        self.assertEqual(2, self.s2.age)

    def test_survivors_doesnt_need_anything_after_creation(self):
        self.assertEqual(False, self.s1.needs_healing)
        self.assertEqual(False, self.s1.needs_sustenance)
        self.assertEqual(False, self.s2.needs_healing)
        self.assertEqual(False, self.s2.needs_sustenance)

    def test_survivors_need_healing_after_damage(self):
        self.s1.health -= 20
        self.s2.health -= 20

        self.assertEqual(True, self.s1.needs_healing)
        self.assertEqual(True, self.s2.needs_healing)

    def test_survivors_need_sustenace_after_needs_decrease(self):
        self.s1.needs -= 20
        self.s2.needs -= 20
        self.assertEqual(True, self.s1.needs_sustenance)
        self.assertEqual(True, self.s2.needs_sustenance)

    def test_survivors_heal_and_medicines_are_reduced_after_heal_is_called(self):
        self.s1.health -= 20
        self.s2.health -= 20
        self.b.heal(self.s1, 'Painkiller')
        self.b.heal(self.s2, 'Painkiller')

        self.assertEqual(False, self.s1.needs_healing)
        self.assertEqual(False, self.s2.needs_healing)
        self.assertEqual(2, len(self.b.painkillers))

    def test_survivors_sustain_and_supplies_are_reduced_after_sustain_is_called(self):
        self.s1.needs -= 20
        self.s2.needs -= 20
        self.b.sustain(self.s1, 'FoodSupply')
        self.b.sustain(self.s2, 'FoodSupply')

        self.assertEqual(False, self.s1.needs_sustenance)
        self.assertEqual(False, self.s2.needs_sustenance)
        self.assertEqual(2, len(self.b.food))

    def test_survivours_needs_and_supplies_are_changed_after_next_day(self):
        self.s1.needs -= 80
        self.s2.needs -= 80
        s1_expected_needs = 76
        s2_expected_needs = 76
        self.b.next_day()
        self.assertEqual(s1_expected_needs, self.s1.needs)
        self.assertEqual(s2_expected_needs, self.s2.needs)
        self.assertEqual(2, len(self.b.food))
        self.assertEqual(2, len(self.b.water))

    def test_bunker_raises_IndexError_when_no_supplies(self):
        self.s1.needs -= 90
        for _ in range(4):
            self.b.sustain(self.s1, 'FoodSupply')

        no_food = 'There are no food supplies left!'
        with self.assertRaises(IndexError) as ef:
            f = self.b.food
            self.assertEqual(no_food, str(ef))

        self.s2.needs -= 90
        for _ in range(4):
            self.b.sustain(self.s2, 'WaterSupply')

        no_water = 'There are no water supplies left!'
        with self.assertRaises(IndexError) as ew:
            w = self.b.water
            self.assertEqual(no_water, str(ew))


if __name__ == "__main__":
    unittest.main()
