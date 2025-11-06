import random
from .player import Player


class Orc(Player):
    def __init__(self, name, hp=50, speed=random.randint(0, 5), power=random.randint(10, 15), armor_rating=random.randint(2, 8), weapon=random.choice(["knife","sword","axe"]), type="orc"):
        super().__init__(name, hp, speed, power, armor_rating)
        self.type = type
        self.weapon = weapon
       
    def speak(self):
        return f"The {self.type}{self.name} is Angry!!!!!!"
    
    def calc_demage_monster_attack(self, shoot):
        damage = 0
        if self.weapon == "knife":
            damage = 0.5
        if self.weapon == "axe":
            damage = 1.5
        else:
            damage = 1

        return damage * shoot

    
    def attack(self, other):
        shoot = (random.randint(1, 20)) + self.speed
        if shoot > other.armor_rating:
            damage = (random.randint(1, 6)) + self.power
            amount_reduce = self.calc_demage_monster_attack(damage)
            self.reduce_life(other, amount_reduce)



    def __str__(self):
        return f"The name is {self.name} he is a {self.type}, is life number is {self.hp}, he has a speed {self.speed}, and has power of {self.power}, is armor rating is {self.armor_rating} and is weapon is {self.weapon}"
    

