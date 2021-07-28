import unittest


class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return (f'{self.name} has saved {self.money} money.')


class WorkerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.w = Worker('Test', 100, 100)

    def test_worker_init(self):
        self.assertEqual('Test', self.w.name)
        self.assertEqual(100, self.w.salary)
        self.assertEqual(100, self.w.energy)

    def test_work_rest(self):
        self.w.rest()
        self.assertEqual(101, self.w.energy)

    def test_worker_raises_if_work_with_zero_energy(self):
        self.w.energy = 0
        with self.assertRaises(Exception) as ctx:
            self.w.work()
            self.assertEqual('Not enough energy.', str(ctx.exception))

    def test_worker_raises_if_work_with_negative_energy(self):
        self.w.energy = -5
        with self.assertRaises(Exception) as ctx:
            self.w.work()
            self.assertEqual('Not enough energy.', str(ctx.exception))

    def test_worker_work_increases_money_by_salary(self):
        self.w.work()
        self.assertEqual(100, self.w.money)

    def test_worker_work_decrease_energy(self):
        self.w.work()
        self.assertEqual(99, self.w.energy)

    def test_worker_get_info(self):
        self.assertEqual('Test has saved 0 money.',self.w.get_info())


if __name__ == "__main__":
    unittest.main()
