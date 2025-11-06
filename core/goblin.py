import random
from .orc import Orc


class Goblin(Orc):
    def __init__(self, name, hp=20, speed=random.randint(5, 10), power=random.randint(5, 10), weapon=random.choice(["knife","sword","axe"]), type="goblin", armor_rating=1):
        super().__init__(name, hp, speed, power, armor_rating, weapon, type)
    

    def speak(self):
        return f"The {self.type}{self.name} is Angry!!!!!!"
    

    def attack(self, other):
        return super().attack(other)

    def __str__(self):
        return super().__str__()
    
