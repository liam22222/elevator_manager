# 1 - Fast
# 2 - Standart
# 3 - Cargo
import builtins
from Building import Building
building = Building(20)
def type_availability(building, req_floor, num_persons, cargo):
    """Reciving - Building, Requested floor, Persons, Cargo\n Return - List of availible types."""
    if req_floor > building.n:
        return []
    types = building.elevators.keys()
    print(types)
building = Building(20)
type_availability(building,10,5,5)