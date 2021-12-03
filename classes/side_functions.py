# 1 - Fast
# 2 - Standart
# 3 - Cargo
import threading
from Building import Building
from Elevator_classes import Elevator
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

    for key in building.elevators.keys():
        if building.elevators[key][0].sub_check(num_persons,cargo,req_floor) == True:
            good_types.append(key)

    return good_types

def find_elevator(building, good_types):
    """Reciving - Building, Types of elevators that can answer a specific request\n Return - Message of the elevator on his way."""
    min = 11 # Min seconeds to wait
    minid = -1

    for elevator_type in good_types:
        #print(f"elevator type: {elevator_type}")
        minTTA = building.elevators[elevator_type][0].tta

        if minTTA == 0:
            #This thread create a reserve
            thread = threading.Thread(target=reserve_first_elevator,args=(building,elevator_type,))
            thread.start()

            #Getting the current information about the first elevator before the cycle
            id = building.elevators[elevator_type][0].id
            information = building.elevators[elevator_type][0].print()
            
            #This commands is poping the first item and appending it in the end
            building.elevators[elevator_type].append(building.elevators[elevator_type].popleft())
            
            return f"\nElevator: {id} is reserved for you!\n{information}"
        else:
            if minTTA < min:
                min = minTTA
                minid = building.elevators[elevator_type][0].id
        
    if minid == -1:
        return "\nThere is no such elevator for this request!"
    else:
        return f"\nThere are no availeble elevators for you right now.\nPlease wait for {minTTA} secondes." 

building = Building(20)
print(type_availability(building, 12, 0, 70))