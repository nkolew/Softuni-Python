from project.worker import Worker
from project.animal import Animal
from project.lion import Lion
from project.tiger import Tiger
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.vet import Vet
from project.caretaker import Caretaker
from project.zoo import Zoo

import unittest

class Tests(unittest.TestCase):
    def test_lion_init(self):
      l = Lion("a", "m", 4)
      self.assertEqual(l.name, "a")
      self.assertEqual(l.gender, "m")
      self.assertEqual(l.age, 4)
      
    def test_lion_get_needs(self):
      l = Lion("b", "f", 2)
      res = l.get_needs()
      self.assertEqual(res, 50)
      
    def test_lion_repr(self):
      l = Lion("b", "f", 2)
      res = str(l)
      self.assertEqual(res, "Name: b, Age: 2, Gender: f")
      
    def test_tiger_init(self):
      t = Tiger("z", "m", 1)
      self.assertEqual(t.name, "z")
      self.assertEqual(t.gender, "m")
      self.assertEqual(t.age, 1)

    def test_tiger_get_needs(self):
      t = Tiger("v", "f", 7)
      res = t.get_needs()
      self.assertEqual(res, 45)
      
    def test_tiger_repr(self):
      t = Tiger("w", "f", 3)
      res = str(t)
      self.assertEqual(res, "Name: w, Age: 3, Gender: f")
      
    def test_cheetah_init(self):
      c = Cheetah("l", "f", 3)
      self.assertEqual(c.name, "l")
      self.assertEqual(c.gender, "f")
      self.assertEqual(c.age, 3)

    def test_cheetah_get_needs(self):
      c = Cheetah("r", "m", 6)
      res = c.get_needs()
      self.assertEqual(res, 60)

    def test_cheetah_repr(self):
      c = Cheetah("n", "f", 2)
      res = str(c)
      self.assertEqual(res, "Name: n, Age: 2, Gender: f")
      
    def test_keeper_init(self):
      k = Keeper("john", 21, 200)
      self.assertEqual(k.name, "john")
      self.assertEqual(k.age, 21)
      self.assertEqual(k.salary, 200)
      
    def test_keeper_repr(self):
      k = Keeper("ally", 36, 190)
      res = str(k)
      self.assertEqual(res, "Name: ally, Age: 36, Salary: 190")

    def test_vet_init(self):
      k = Vet("john", 21, 200)
      self.assertEqual(k.name, "john")
      self.assertEqual(k.age, 21)
      self.assertEqual(k.salary, 200)
      
    def test_vet_repr(self):
      k = Vet("ally", 36, 190)
      res = str(k)
      self.assertEqual(res, "Name: ally, Age: 36, Salary: 190")

    def test_caretaker_init(self):
      k = Caretaker("john", 21, 200)
      self.assertEqual(k.name, "john")
      self.assertEqual(k.age, 21)
      self.assertEqual(k.salary, 200)
      
    def test_caretaker_repr(self):
      k = Caretaker("ally", 36, 190)
      res = str(k)
      self.assertEqual(res, "Name: ally, Age: 36, Salary: 190")

      
    def test_zoo_init(self):
      z = Zoo("My Zoo", 1500, 6, 10)
      self.assertEqual(z._Zoo__animal_capacity, 6)
      self.assertEqual(z._Zoo__workers_capacity, 10)
      self.assertEqual(z._Zoo__budget, 1500)
      self.assertEqual(z.name, "My Zoo")
      self.assertEqual(z.animals, [])
      self.assertEqual(z.workers, [])
      
      
    def test_zoo_add_animal_success(self):
      z = Zoo("My Zoo", 1500, 6, 10)
      res = z.add_animal(Lion("Neo", "Male", 2), 1000)
      self.assertEqual(res, "Neo the Lion added to the zoo")
      self.assertEqual(len(z.animals), 1)
      self.assertEqual(z._Zoo__budget, 500)
      
    def test_zoo_add_animal_no_budget(self):
      z = Zoo("My Zoo", 500, 6, 10)
      res = z.add_animal(Lion("Neo", "Male", 2), 1000)
      self.assertEqual(res, "Not enough budget")
      self.assertEqual(len(z.animals), 0)
      self.assertEqual(z._Zoo__budget, 500)
      
    def test_zoo_add_animal_no_space(self):
      z = Zoo("My Zoo", 1500, 0, 10)
      res = z.add_animal(Lion("Neo", "Male", 2), 1000)
      self.assertEqual(res, "Not enough space for animal")
      self.assertEqual(len(z.animals), 0)
      self.assertEqual(z._Zoo__budget, 1500)
      
    def test_zoo_hire_worker_success(self):
      z = Zoo("Some Zoo", 1500, 1, 1)
      res = z.hire_worker(Vet("I am Vet", 20, 500))
      self.assertEqual(res, "I am Vet the Vet hired successfully")
      self.assertEqual(len(z.workers), 1)
      self.assertEqual(z._Zoo__workers_capacity, 1)

    def test_zoo_hire_worker_no_space(self):
      z = Zoo("Some Zoo", 1500, 1, 0)
      res = z.hire_worker(Vet("I am Vet", 20, 500))
      self.assertEqual(res, "Not enough space for worker")
      self.assertEqual(len(z.workers), 0)
      self.assertEqual(z._Zoo__workers_capacity, 0)
      
    def test_zoo_fire_worker_success(self):
      z = Zoo("Zoo", 1500, 1, 1)
      z.hire_worker(Keeper("K", 45, 100))
      res = z.fire_worker("K")
      self.assertEqual(res, "K fired successfully")
      self.assertEqual(z.workers, [])

    def test_zoo_fire_worker_unsuccessful(self):
      z = Zoo("Zoo", 1500, 1, 1)
      res = z.fire_worker("K")
      self.assertEqual(res, "There is no K in the zoo")
      self.assertEqual(z.workers, [])
      
    def test_zoo_pay_worker_success(self):
      z = Zoo("Zoo", 1500, 2, 2)
      z.hire_worker(Vet("John", 23, 100))
      z.hire_worker(Keeper("Bill", 28, 150))
      res = z.pay_workers()
      self.assertEqual(z._Zoo__budget, 1250)
      self.assertEqual(res, "You payed your workers. They are happy. Budget left: 1250")
      
    def test_zoo_pay_worker_no_budget(self):
      z = Zoo("Zoo", 200, 2, 2)
      z.hire_worker(Vet("John", 23, 100))
      z.hire_worker(Keeper("Bill", 28, 150))
      res = z.pay_workers()
      self.assertEqual(res, "You have no budget to pay your workers. They are unhappy")
      
    def test_zoo_tend_animal_success(self):
      z = Zoo("Zoo", 500, 2, 2)
      z.add_animal(Lion("John", "m", 2), 100)
      z.add_animal(Tiger("Bill", "f", 4), 100)
      res = z.tend_animals()
      self.assertEqual(z._Zoo__budget, 205)
      self.assertEqual(res, "You tended all the animals. They are happy. Budget left: 205")

    def test_zoo_tend_animal_no_budget(self):
      z = Zoo("Zoo", 250, 2, 2)
      z.add_animal(Lion("John", "m", 2), 100)
      z.add_animal(Tiger("Bill", "f", 4), 100)
      res = z.tend_animals()
      self.assertEqual(res, "You have no budget to tend the animals. They are unhappy.")
      
    def test_zoo_profit(self):
      z = Zoo("Mine", 250, 2, 2)
      z.profit(250)
      self.assertEqual(z._Zoo__budget, 500)
      
    def test_animal_status(self):
      z = Zoo("My Zoo", 500, 3, 3)
      z.add_animal(Lion("Leo", "Male", 3), 100)
      z.add_animal(Tiger("Tigy", "Female", 4), 100)
      z.add_animal(Cheetah("Chi", "Female", 2), 100)
      res = z.animals_status()
      self.assertEqual(res, "You have 3 animals\n----- 1 Lions:\nName: Leo, Age: 3, Gender: Male\n----- 1 Tigers:\nName: Tigy, Age: 4, Gender: Female\n----- 1 Cheetahs:\nName: Chi, Age: 2, Gender: Female")

    def test_worker_status(self):
      z = Zoo("My Zoo", 500, 3, 3)
      z.hire_worker(Vet("Leo", 35, 100))
      z.hire_worker(Keeper("Tigy", 40, 100))
      z.hire_worker(Caretaker("Chi", 24, 100))
      res = z.workers_status()
      self.assertEqual(res, "You have 3 workers\n----- 1 Keepers:\nName: Tigy, Age: 40, Salary: 100\n----- 1 Caretakers:\nName: Chi, Age: 24, Salary: 100\n----- 1 Vets:\nName: Leo, Age: 35, Salary: 100")
      
if __name__ == "__main__":
   unittest.main()