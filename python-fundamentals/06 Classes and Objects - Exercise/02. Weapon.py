class Weapon:
    def __init__(self, bullets: int) -> None:
        self.bullets = bullets

    def shoot(self):
        if self.bullets == 0:
            return 'no bullets left'
        self.bullets -= 1
        return 'shooting...'

    def __repr__(self) -> str:
        return f'Remaining bullets: {self.bullets}'


weapon = Weapon(5)
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
print(weapon)
