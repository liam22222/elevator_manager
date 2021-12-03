import requests
import time
BASE = "http://127.0.0.1:5000"
print(requests.post(BASE + "/getElevators/2").json()["data"])
time.sleep(1)
print(requests.post(BASE + "/getElevators/2").json())
time.sleep(1)
print(requests.post(BASE + "/getElevators/2").json())
time.sleep(1)
print(requests.post(BASE + "/getElevators/2").json())

#response2 =  requests.post(BASE + "/getElevators/2")