import random


class Player:
    def __init__(self, name, hp=50, speed=random.randint(5, 10), power=random.randint(5, 10), armor_rating=random.randint(5, 15)):
        self.name = name
        self.speed = speed 
        self.armor_rating = armor_rating
        self.profession = random.choice(["doctoer", "fighter"])
        if self.profession == "doctor":
            self.hp = (hp + 10)
            self.power = power
        else:
            self.hp = hp 
            self.power=random.randint(5, 12)


    def speak(self):
        return f"Hi my name is {self.name}"

    
    def reduce_life(self, other, amount):
        other.hp -= amount
        return other
    

    def attack(self, other):
        shoot = (random.randint(1, 20)) + self.speed
        if shoot > other.armor_rating:
            damage = (random.randint(1, 6)) + self.power
            self.reduce_life(other, damage)



    def __str__(self):
        return f"The name is {self.name} he is a {self.profession}, is life number is {self.hp}, he has a speed {self.speed}, and has power of {self.power}, is armor rating is {self.armor_rating}"
    
