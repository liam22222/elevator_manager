import requests
import time
BASE = "http://127.0.0.1:5000"

#Persons/Cargo/Floor

answer = input("Would you like to enter the terminal mode(yes/no)? (no is deafult): ")
if answer == "yes":
    print("Youre now entering the Terminal mode.\nPlease make sure to enter values by order of:\nNumber of persons -> int\nWeight of cargo -> int\nRequested floor -> int\nAlso, make sure to use space between them.")
    while(True):
        people,cargo,floor = input("\nEnter your values: ").split()
        print(requests.get(BASE + f"/getElevators/{people}/{cargo}/{floor}").json()["data"])
else:  
    #Your code here...
    print(requests.get(BASE + "/getElevators/2/40/7").json()["data"])
    print(requests.get(BASE + "/getElevators/2/40/7").json()["data"])
    print(requests.get(BASE + "/getElevators/2/40/7").json()["data"])
