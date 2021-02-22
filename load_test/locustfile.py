from locust import HttpUser, TaskSet, task
import json
import random

featureList = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

class MyUser(HttpUser):
	@task(1)
	def get_tests(self):
		dataBody = {}
		for feature in featureList:
			dataBody[feature] = round(random.uniform(0.1, 10),3)
		self.client.post("/", data= json.dumps(dataBody))
				