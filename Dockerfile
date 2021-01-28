# set base image (host OS)
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./requirements.txt ./requirements.txt

RUN pip install fastapi uvicorn
RUN pip install -r requirements.txt

COPY ./model ./model
COPY ./scaler ./scaler
COPY ./src ./src

EXPOSE 8005

WORKDIR ./src