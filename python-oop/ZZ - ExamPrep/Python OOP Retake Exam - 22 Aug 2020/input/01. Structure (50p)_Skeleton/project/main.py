from rooms.young_couple import YoungCouple
from rooms.young_couple_with_children import YoungCoupleWithChildren

from people.child import Child

from everland import Everland

everland = Everland()

def test_one():
    young_couple = YoungCouple("Johnsons", 150, 205)

    child_one = Child(5, 1, 2, 1)
    child_two = Child(3, 2)
    young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child_one, child_two)

    everland.add_room(young_couple)
    everland.add_room(young_couple_with_children)

    print(everland.get_monthly_consumptions())
    print(everland.pay())
    print(everland.status())


if __name__ == "__main__":
    test_one()