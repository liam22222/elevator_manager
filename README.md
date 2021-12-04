# StarGo elevator manager project - Liam Ashkneazi
## server.py 
The server.py is the RESTful api that simply listen to any get request on localhost:5000 for elevators reservation. 
The expected request format is: `http://127.0.0.1:5000/getElevators/<int:num_persons>/<int:cargo_weight>/<int:requested_floor>`

Once a request was listed, a function named `find_elevator` with help of `type_availability` are in search for an elevator
that can handle the request. In order to understand the function and how they work, we need to go deeper in this code.
```
def get(self, num_persons, cargo_weight, requested_floor):
        return {"data" : find_elevator(building,
        type_availability(
            building=building,
            req_floor=requested_floor,
            num_persons=num_persons,
            cargo=cargo_weight)
        )}
```
## Classes in the code (OOP and OOD)
### Elevator and his sub-classes (FastElevator, StandartElevator, CargoElevator)
`Elevator` is a class in the project that handles all there is to know about elevators id, maxium number of persons, weight of cargo and the most importand, Time till availability (TTA)

This class has three sub-classes that are configured using the elevator properties, yet, each have a diffrent role in
the project. You can read more about them in [the code](https://github.com/liam22222/elevator_manager/blob/main/classes/Elevator_classes.py), but here is an example
of `FastElevator.__init__` that configure a simple elevator with limitation of only able to travel for the ten story and upwards with max persons of five people
```
class FastElevator(Elevator):
    def __init__(self, id):
        """Initalize an elevator with fast elevator characteristics"""
        super().__init__(id, 5, 0)
        self.min_floor = 10
```

### Building class
The building class is responsible for the all elevators managment and contain a proprety of elevators. This special
proprety is a `dict{int : deque}` and the reason why such an odd use of collection is related to the **efficiency**.
It will be explained later on this document.

The building takes for granted the fact that there is at least one elevator for each type of elevators, but, his
``__init__`` also randomized one to three more elevators. 
```
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
```
## The functions that made it all
**There are two functions that act as the brain of the server. We are going to explain each for now**
### [Type availability](https://github.com/liam22222/elevator_manager/blob/main/classes/side_functions.py#L8)
Lets say the user entered a request as such. I want to go to the eleven floor, with no Cargo and two other people. 
Who can handle this request? and what about (2,0,0)? why should I handle this request?
The Type abailability checks which sub-class of elevators are able to handle this request. He does it with `sub_check`
which is a function written down in every sub-class and returns wether this class is able to help or no. 
I used this command in order to keep the OOD of this project insted of developing a fixed solution.
```
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

```
### [Find elevator](https://github.com/liam22222/elevator_manager/blob/main/classes/side_functions.py#L22)
Now that we know who can handle our request, it is time to reserve an elevator for it right?
Imagine we have a tenant lives in the eleven floor, and our system reserve him a standart elevator. What?
This function gives priority to which elevator should I use using the elevator priority(fast, standart, cargo), and time to wait.
So lets say that our function detact that it is better to send a fast elevator insted of a standart one. How is it know which one to send? If it want to check which elevator is the closes it need to check in each and every one of them what is thier TTA, it will take `O(N-number of elevators from the same type)`.
This is why I used `dict{int : deque}`.
When I figured out that a certin type is the best for a request, I told the first elevator from this type to handle it. Then, I set her TTA to be 10, and used `deque.leftpop()` to pop it and `deque.append()` to add it to the right.
If the first elevator in some type TTA value is'nt 0, the all elevators from this type are in used and maybe I should use another type of elevators if possible for this request.
I do understand it is hard to figure it out from the text, so, here is an example.

Lets say I have this as configured elevators in my building: 
```
Fast type ->
        Id: 1, TTA: 3
Standart type ->
        Id: 2, TTA: 0
        Id: 3, TTA: 4
```
When requesting the following (13, 2, 0) (13 floor, two people, no cargo) Both standart and fast type of elevators can help. At first, the code tries to find a fast elevator but he sees that its TTA set to 3 so he set minimum value of waiting to be 3.
Then, he found out that in the standart type there is an elevator with 0 TTA which mean its free to use. So the code reserve it, returning it to the user, and edit the data inside the Building object to be like so: 

```
Fast type ->
        Id: 1, TTA: 2
Standart type ->
        Id: 3, TTA: 3
        Id: 2, TTA: 10
```
As you see now, the number 3 elevator is ahead of number 2 elevator which make sense. 
## Class diagram and sequence diagram
### Class diagram
![image](https://user-images.githubusercontent.com/34837970/144663060-e783caa5-27a4-4678-a629-94150ef4dc99.png)
### Sequence diagram
![image](https://user-images.githubusercontent.com/34837970/144665113-a706469c-7a97-4bf4-bcf3-cde1c5aa0bcd.png)


## Key concepts 
### Threading
In order to make sure a reserve of an elevator wont steal my processor attention I used threading. It is when you manage a child process to make a job for you and the main code keep on going. You can read more about the **mutex** logic behined it in [here](https://en.wikipedia.org/wiki/Lock_(computer_science))

### Deque 
Deque is a double ended queue which fit perfectly to the situation I need to develop. Using its `O(1)` popleft() and append() methods allowed me to quick serch a bunch of elevators insted of `O(n*m)` where m is the number of elevators from a specific type and n is the type. Now all I have to do, is search from the list of allowed elevators type which in worst case would be `O(n)`.
