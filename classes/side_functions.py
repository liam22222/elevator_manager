# 1 - Fast
# 2 - Standart
# 3 - Cargo
import threading
from Building import Building
building = Building(20)
def reserve_first_elevator(building, elevator_type):
    building.elevators[elevator_type][0].reserve()

def type_availability(building, req_floor, num_persons, cargo):
    """Reciving - Building, Requested floor, Persons, Cargo\n Return - List of availible types."""
    if req_floor > building.n:
        return [] # You cant get out the building
    if num_persons == 0 and cargo == 0:
        return [] # We wont waste time for no cargo and no persons
    good_types = [] # Types that can handle the request
    if req_floor >= 10 and num_persons <= 5 and cargo == 0:
        good_types.append(1)
    if num_persons <= 10 and cargo <= 50:
        good_types.append(2)
    if req_floor%2 == 1 and num_persons == 0 and cargo <= 750:
        good_types.append(3)
    return good_types

def find_elevator(building, good_types):
    """Reciving - Building, Types of elevators that can answer a specific request\n Return - Message of the elevator on his way."""
    min = 10
    for elevator_type in good_types:
        minTTA = building.elevators[elevator_type]
        if building.elevators[elevator_type][0].tta == 0:
            #This thread create a reserve
            thread = threading.Thread(target=reserve_first_elevator,args=(building,elevator_type,))
            thread.start()

            #Getting the current information about the first elevator before the cycle
            id = building.elevators[elevator_type][0].id
            information = building.elevators[elevator_type][0].print()

            #This command is poping the first item and appending it in the end
            building.elevators[elevator_type].append(building.elevators[elevator_type].popleft)
            return f"Elevator: {id} is reserved for you!\n{information}"


building = Building(20)
print(building.elevators["1"][0].tta)
print(type_availability(building,7,11,0))