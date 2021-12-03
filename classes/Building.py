import random
from Elevator_classes import FastElevator, StandartElevator, CargoElevator

class Building:
    def __init__(self, n):
        self.n = n
        self.elevators = [ # The building will automaticly have three elevators at least
            FastElevator(1),
            StandartElevator(2),
            CargoElevator(3)
        ]
        for id in range(random.randint(1,3)):
            randomElevator = random.randint(1,3)
            print(f"Id: {id+4}, Random: {randomElevator}")
            if randomElevator == 1:
                self.elevators.append(FastElevator(id+4))
            if randomElevator == 2:
                self.elevators.append(StandartElevator(id+4))
            if randomElevator == 3:
                self.elevators.append(CargoElevator(id+4))
    def print(self):
        print(f"This building has {self.n} floors\nThe elevators are: ")
        for ele in self.elevators:
            print(f"\nElevator {ele.id}: {type(ele)}")
            
        
building = Building(20)
building.print()