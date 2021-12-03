import time

class Elevator():
    def __init__(self, id, max_persons, max_cargo):
        """Id - elevator id\n
        max_persons - The number of allowed persons in this elevator\n
        max_cargo - Same as max_persons for cargo in KG\n
        tta - time till aveilibale\n"""
        self.id = id 
        self.max_persons = max_persons
        self.max_cargo = max_cargo
        self.tta = 0

    def print(self):
        """Print information about our elevator"""
        return (f"Elevator id: {self.id}\nMax persons: {self.max_persons}\nMax cargo: {self.max_cargo}")

    def reserve(self):
        """Reserve function make a holding for the elevator which mean it cant be in use in Those 10 secondes.\nIt handles like a mutex in Operation systems"""
        print(f"Elevator {self.id} Has been reserved...")
        self.tta = 10
        while(self.tta > 0):
            self.tta -= 1
            time.sleep(1)

class FastElevator(Elevator):
    def __init__(self, id):
        """Initalize an elevator with fast elevator characteristics"""
        super().__init__(id, 5, 0)
    
    def print(self):
        return "Fast Elevator\n" + super().print()

    def reserve(self):
        return super().reserve()

class StandartElevator(Elevator):
    def __init__(self, id):
        super().__init__(id, 10, 50)
    
    def print(self):
        """Initalize an elevator with standart elevator characteristics"""
        return "Standart Elevator\n" + super().print()

    def reserve(self):
        return super().reserve()

class CargoElevator(Elevator):
    def __init__(self, id):
        super().__init__(id, 0, 750)

    def print(self):
        """Initalize an elevator with cargo elevator characteristics"""
        return "Cargo Elevator\n" + super().print()

    def reserve(self):
        return super().reserve()
