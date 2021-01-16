# set base image (host OS)
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./requirements.txt ./requirements.txt
COPY ./src ./src

RUN pip install fastapi uvicorn
RUN pip install -r requirements.txt

COPY ./model ./model
COPY ./scaler ./scaler

EXPOSE 8005

WORKDIR ./src

# command to run on container start
#CMD ["ls", "-la", "."]
#CMD ["uvicorn", "main:app", "--port", "8005", "--reload"]