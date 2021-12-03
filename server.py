import threading
from flask import Flask
from classes.Building import Building
from flask_restful import Api, Resource
from classes.Elevator_classes import FastElevator, StandartElevator, CargoElevator

app = Flask(__name__)
api = Api(app)

building = Building(20) # Creating a building with random elevators in it

myElevators = {
    1 : FastElevator(1),
    2 : StandartElevator(2),
    3 : CargoElevator(3)
}

def reserve_elevator(id):
    myElevators[id].reserve()

class getElevators(Resource):
    def get(self, id):
        return {"Data": myElevators[id].print()}
    
    def post(self, id):
        if myElevators[id].tta == 0:
            thread = threading.Thread(target = reserve_elevator, args=(id,))
            thread.start()
            return {"data" : f"Elevator {id} is on your way!\nThier detailes are {myElevators[id].print()}"}
        else:
            return {"data" : f"Elevator {id} is currently busy and could not be reserved.\nPlease wait for {myElevators[id].tta} secondes."}


api.add_resource(getElevators, "/getElevators/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)