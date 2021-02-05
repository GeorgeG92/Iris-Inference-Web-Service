from locust import HttpUser, TaskSet, task
import json

dataBody = {'SepalLengthCm':5.1, 'SepalWidthCm':3.5,
        'PetalLengthCm':1.4 , 'PetalWidthCm':0.2}

class MyUser(HttpUser):
    @task(1)
    def get_tests(self):
        self.client.get("/", data= json.dumps(dataBody))
                