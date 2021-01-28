# Iris-Inference-Web-Service
The project includes code for serving an XGBoost multi-class classifier trained on the Iris dataset, served through a fastAPI interface.

## Run web server
```
cd src
uvicorn main:app --port 8005 (--reload)
```
or through Docker
```
docker-compose up
```

## Run Unit Tests
Simply, run from root:
```
pytest
```
## Load testing using Locust

### Run Locust service
```
cd src
locust --host=http://localhost:8005 -f locustfile.py
```
### Start load test

Navigate to http://localhost:8089/ and start swarming

## Manually test the Api 

### Through jupyter notebook

Run the last cell of Model Train.ipynb in the jupyter folder

### Through python code

``` Python
session = requests.Session()
session.trust_env = False

data = {'SepalLengthCm':5.1, 'SepalWidthCm':3.5,
        'PetalLengthCm':1.4 , 'PetalWidthCm':0.2}

tries = 100
start = time.time()
for i in range(tries):
    response = session.get('http://localhost:8005', json=data)
    #print(response.json())
    continue
end = time.time()
elapsed = round(end-start,3)
reqsPerSec = round(float(tries/elapsed),3)
print("Elapsed time:", elapsed,"seconds,", reqsPerSec,"requests/sec") 
```
