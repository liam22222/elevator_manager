from flask import Flask
from classes.Building import Building
from flask_restful import Api, Resource
from classes.side_functions import type_availability, find_elevator

app = Flask(__name__)
api = Api(app)

building = Building(20)

class getElevators(Resource):
    def get(self, num_persons, cargo_weight, requested_floor):
        return {"data" : find_elevator(building,
        type_availability(
            building=building,
            req_floor=requested_floor,
            num_persons=num_persons,
            cargo=cargo_weight)
        )}


api.add_resource(getElevators, "/getElevators/<int:num_persons>/<int:cargo_weight>/<int:requested_floor>")

if __name__ == "__main__":
    app.run(debug=True)