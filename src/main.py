import numpy as np
import os
import pandas as pd
from model import xgbModel
from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()
model = xgbModel()

class dataPoint(BaseModel):
	SepalLengthCm: float
	SepalWidthCm: float
	PetalLengthCm: float
	PetalWidthCm: float


def prepareResponse(pred):
	""" Parse the prediction into a dictionary to be returned """
	responseDict = {'prediction': pred}
	return responseDict

@app.get('/')
async def getPrediction(dp: dataPoint):
	#print("\tgetPrediction:",dp)
	prediction = model.infer(dp)
	#print("\tprediction is ",prediction)
	responseDict = prepareResponse(prediction)  
	return responseDict 