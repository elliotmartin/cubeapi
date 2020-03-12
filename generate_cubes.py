import Rubik
import requests
import time

for i in range(10000):
    random_cube = Rubik.generate_cube()
    requests.post("http://localhost:8000/api/cubes/",
                  data ={'cube':str(random_cube)},
                  auth=requests.auth.HTTPBasicAuth('elliot','PASSWORD'))
