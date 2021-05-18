import random
import time
class Board:
    def __init__(self):
        self.__Snake = {99:7, 41:20, 84:65, 50:5, 89:58, 73:15, 37:1}
        self.__Ladder = {3:60, 6:27, 35:56, 11:71, 68:93, 63:96, 51:67}
    
    def roll(self):
        return random.randint(1,6)
    
    def chance(self, position):
        if position in self.__Snake.keys():
            return self.__Snake[position]
        if position in self.__Ladder.keys():
            return self.__Ladder[position]
        return position

class Player(Board):
    __idx = 0
    game_over = 0
    def __init__(self, name):
        self.__position = 0;
        self.name = name
        Player.game_over = 0
        Player.__idx = 0
        super().__init__()
    
    def step(self):
        rolled = self.roll()
        print("Dice :",rolled)
        time.sleep(1)
        if self.__position+rolled<=100:
            self.__position += rolled
            self.__position = self.chance(self.__position)
        Player.__idx += 1
        print("At step:", Player.__idx," Player:", self.name," is at", self.__position)
        if self.__position == 100 :
            time.sleep(1)
            print("Player:",self.name," WON")
            print("GAME OVER")
            Player.game_over = 1

j = int(input("Number of players: "))
Players = []
for i in range(j):
    n = input("Name of player: ")
    Players.append(Player(n))
i = 0
while Player.game_over==0 :
    Players[i].step()
    i+=1
    i = i%len(Players)