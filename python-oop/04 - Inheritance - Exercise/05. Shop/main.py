from project.drink import Drink
from project.food import Food
from project import ProductRepository


pr = ProductRepository()

pizza = Food('pizza')
beer = Drink('beer')

pizza.increase(1)
beer.decrease(2)

pr.add(beer)
pr.add(pizza)

print('-'*8)

print(pr)
pr.remove('pizza')

print('-'*8)

print(pr)
