import random

from core.goblin import Goblin
from core.orc import Orc
from core.player import Player


class Game:

    def show_menu(self):
        print("game over") 

    def create_player(self):
        return Player(input("Enter player name "))

    def choose_random_monster(self): 
        choice = random.choice([Orc, Goblin])
        monster = choice(input("Enter monster name "))
        return monster


    def roll_dice(self, sides):
        return random.randint(1, sides)


    def roll_to_start(self, player: Player, monster: Orc):
        player = self.roll_dice(6) + player.speed
        print(player)
        monster = self.roll_dice(6) + monster.speed
        print(monster)
        if player > monster or player == monster:
            return "player starts"
        else:
            return "monster starts" 

    def end_game(slef, player: Player, monster: Orc):
        return player.hp <= 0 or monster.hp <= 0     

    def battle(self, player: Player, monster: Orc, res):
        if res == "player start":
            player.attack(monster)
            print(f"monster life remain is {monster.hp}")
            monster.attack(player)
            print(f"player life remain is {player.hp}")
        else:
            monster.attack(player)
            print(f"player life remain is {player.hp}")
            player.attack(monster)
            print(f"monster life remain is {monster.hp}")
              
    

    def start(self):
        print("welcome")
        player = self.create_player()
        print(f"Hi {player.name}")
        monster = self.choose_random_monster()
        print(f"Hi {monster.name}")
        res = self.roll_to_start(player, monster)
        count = 1
        while not self.end_game(player, monster):
           print(f"---- Round {count} ----")
           self.battle(player, monster, res)
           count += 1
        self.show_menu()
   