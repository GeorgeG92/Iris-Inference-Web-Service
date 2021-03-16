/github/workflow/status/:GeorgeG92/:Iris-Inference-Web-Service/:XGB-Classifier-CI
# Iris-Inference-Web-Service
The project includes code for serving an XGBoost multi-class classifier trained on the Iris dataset, served through a docker-enabled fastAPI interface.Additionally, it includes pytest unit tests as well as load testing on the deployed service through through locust. Requirements can be extracted using pipreqs, by running the following command at the project root folder: 
```sh
pipreqs --encoding=utf8 ./
```

# Run web server
```sh
cd src
uvicorn main:app --port 8006 (--reload)
```
or using docker-compose:
```sh
docker-compose up
```
using the specified host and container ports from the .env file. Afterwards, you can navigate the generated docs, experiment with the API's capabilities and behavior through the Swagger UI on http://localhost:port/docs, in the default case being http://localhost:8006/docs  

# Run test suite
From the root project folder:
```sh
pytest
```

# Load testing using Locust

## Run Locust service
```sh
cd load_test
locust --host=http://localhost:8006 -f locustfile.py
```
## Start load test

Navigate to http://localhost:8089/ and start swarming through locust

# Manually test the Api 

## Through jupyter notebook

Run the Model Train.ipynb in the jupyter folder

## Through python code

```python
import requests
import time

session = requests.Session()
session.trust_env = False

data = {'SepalLengthCm':5.1, 'SepalWidthCm':3.5,
        'PetalLengthCm':1.4 , 'PetalWidthCm':0.2}

tries = 100
start = time.time()
for i in range(tries):
    response = session.get('http://localhost:8006', json=data)
    #print(response.json())
    continue
end = time.time()
elapsed = round(end-start,3)
reqsPerSec = round(float(tries/elapsed),3)
print("Elapsed time:", elapsed,"seconds,", reqsPerSec,"requests/sec") 
```
