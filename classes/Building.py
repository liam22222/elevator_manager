import random
from collections import deque
from .Elevator_classes import FastElevator, StandartElevator, CargoElevator

class Building:
    def __init__(self, n):
        self.n = n 
        self.elevators = { # The building will automaticly have three elevators at least
            1 : deque([FastElevator(1)]),
            2 : deque([StandartElevator(2)]),
            3 : deque([CargoElevator(3)])
        }
        for id in range(random.randint(1,3)):
            randomElevator = random.randint(1,3)
            if randomElevator == 1:
                self.elevators[1].append(FastElevator(id+4))
            if randomElevator == 2:
                self.elevators[2].append(StandartElevator(id+4))
            if randomElevator == 3:
                self.elevators[3].append(CargoElevator(id+4))
    def print(self):
        print(f"This building has {self.n} floors\nThe elevators are: ")
        for tye in self.elevators:
            print(len(self.elevators[tye]))
            
        