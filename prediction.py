import numpy as np
import pickle
loadedModel = pickle.load(open('./trainingmodel.sav','rb'))
inputData = np.array([71,0,0,112,149,0,1,125,0,1.6,1,0,2]).reshape(1,-1)
prediction = loadedModel.predict(inputData)
if prediction[0] == 1:
    print('The Person has a heart disease')
else:
    print('The person does not have a heart disease')