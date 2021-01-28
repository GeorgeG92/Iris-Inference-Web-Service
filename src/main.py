import os
import sys

CURR_DIR = os.path.dirname(os.path.abspath(__file__))        # used for testing
print(CURR_DIR)
sys.path.append(CURR_DIR)

import pandas as pd
import numpy as np
from model import xgbModel
from typing import Optional, List
from fastapi import APIRouter
from fastapi import FastAPI, Query, Path, Cookie, Header, HTTPException, status
from pydantic import BaseModel, Field
from enum import Enum

app = FastAPI()
model = xgbModel()

# Response model
class prediction(BaseModel):
	prediction: str

# Request Model
class dataPoint(BaseModel):
	SepalLengthCm: float = Field(None, title="Sepal Length is >=0", gt=0, lt=1000, example=1.1)
	SepalWidthCm: float = Field(None, description="Sepal Width is >=0", gt=0, lt=1000, example=2.2)
	PetalLengthCm: float = Field(None, description="Pedal Length is >=0", gt=0, lt=1000, example=3.3)
	PetalWidthCm: float = Field(None, description="Pedal Width is >=0", gt=0, lt=1000, example=4.4)


# Endpoint that listens for POST requests on '/'. Requires json body content
@app.post('/', response_model=prediction, status_code=200)
async def get_prediction(dp: dataPoint):
	prediction = model.infer(dp)
	return {'prediction': prediction} 

