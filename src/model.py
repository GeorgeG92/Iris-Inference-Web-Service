import joblib
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
import os
import numpy as np


class xgbModel():
	def __init__(self, modelPath=os.path.join('..', 'model'), modelName='xgb.model', scalerPath=os.path.join('..', 'scaler'), scalerName='std_scaler.bin'):
		""" Initialize model and scaler parameters """
		print("\tLoading Model")
		self.modelPath = os.path.join(modelPath, modelName)
		self.scalerPath = os.path.join(scalerPath, scalerName)
		assert os.path.exists(self.modelPath), "modelPath "+str(self.modelPath)+" is invalid"
		assert os.path.exists(self.scalerPath), "scalerPath "+str(self.scalerPath)+" is invalid"
		self.model = joblib.load(self.modelPath) 
		self.scaler = joblib.load(self.scalerPath)

	def object2numpy(self, data):
		""" Convert object values to a numpy array """
		sl = data.SepalLengthCm
		sw = data.SepalWidthCm
		pl = data.PetalLengthCm
		pw = data.PetalWidthCm
		return np.array([[sl, sw, pl, pw]])

	def standardScale(self, data):
		""" Use the fitted scaler to transform the inference data """
		return self.scaler.transform(data)


	def infer(self, data):
		""" Use the pretrained model to infer the requested example """
		npdata = self.object2numpy(data)
		scaledData = self.standardScale(npdata)
		prediction = self.model.predict(scaledData)
		return prediction[0]

	