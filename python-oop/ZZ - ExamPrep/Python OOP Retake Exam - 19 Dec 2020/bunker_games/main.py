from project import *

b = Bunker()

survivors = [Survivor('one', 2), Survivor('two', 2)]

food = [FoodSupply(), FoodSupply(), FoodSupply(), FoodSupply()]
water = [WaterSupply(), WaterSupply(), WaterSupply(), WaterSupply()]
painkillers = [Painkiller(), Painkiller(), Painkiller(), Painkiller()]
salves = [Salve(), Salve(), Salve(), Salve()]

for p in survivors:
    b.add_survivor(p)

for f in food:
    b.add_supply(f)

for w in water:
    b.add_supply(w)

for p in painkillers:
    b.add_medicine(p)

for s in salves:
    b.add_medicine(s)


assert len(b.survivors) == 2
assert len(b.food) == 4
assert len(b.water) == 4
assert len(b.painkillers) == 4
assert len(b.salves) == 4

assert b.survivors[0].name == 'one'
assert b.survivors[0].needs_healing is False
assert b.survivors[0].needs_sustenance is False

assert b.survivors[1].name == 'two'
assert b.survivors[1].needs_healing is False
assert b.survivors[1].needs_sustenance is False


b.survivors[0].health -= 20
b.survivors[1].health -= 20
b.survivors[0].needs -= 20
b.survivors[1].needs -= 20


assert b.survivors[0].needs_healing is True
assert b.survivors[0].needs_sustenance is True

assert b.survivors[1].needs_healing is True
assert b.survivors[1].needs_sustenance is True

b.heal(b.survivors[0], 'Painkiller')
b.heal(b.survivors[1], 'Painkiller')
assert len(b.painkillers) == 2

assert b.survivors[0].needs_healing is False
assert b.survivors[0].needs_sustenance is True

assert b.survivors[1].needs_healing is False
assert b.survivors[1].needs_sustenance is True


b.sustain(b.survivors[0], 'FoodSupply')
b.sustain(b.survivors[1], 'FoodSupply')
assert len(b.food) == 2

assert b.survivors[0].needs_healing is False
assert b.survivors[0].needs_sustenance is False

# assert b.survivors[1].name == 'two'
# assert b.survivors[1].needs_healing is False
# assert b.survivors[1].needs_sustenance is False
