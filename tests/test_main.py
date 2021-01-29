import sys
import os
sys.path.append("..")
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_get_prediction_ok():
	json_body = {"SepalLengthCm": 4.2,"SepalWidthCm": 1.1, "PetalLengthCm": 2.2, "PetalWidthCm": 3.3}
	response = client.post("/", json=json_body)
	assert "prediction" in response.json()

def test_get_prediction_negative():
	json_body = {"SepalLengthCm": 1.1,"SepalWidthCm": -1, "PetalLengthCm": 3.3, "PetalWidthCm": 4.4}
	response = client.post("/", json=json_body)
	assert response.status_code == 422
	assert "ensure this value is greater than 0" in response.json()['detail'][0]['msg']

def test_get_prediction_wrong_type():
	json_body = {"SepalLengthCm": 1.1,"SepalWidthCm": 15, "PetalLengthCm": 'wrong', "PetalWidthCm": 4.4}
	response = client.post("/", json=json_body)
	assert response.status_code == 422
	assert "value is not a valid float" in response.json()['detail'][0]['msg']
