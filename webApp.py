import numpy as np
import pickle
import streamlit as st
loadedModel = pickle.load(open('trainingModel.sav','rb'))
def heartDiseasePrediction(inputData):
    inputData = np.asarray(inputData).reshape(1,-1)
    prediction = loadedModel.predict(inputData)
    print(prediction[0])
    if prediction[0] == 1:
        return 'The Person has a heart disease'
    else:
        return 'The person does not have a heart disease'

def main():
    st.title('Heart Disease Prediction Web App')
    age = st.number_input('Age of Patient')
    sex = st.number_input('Sex of Patient')
    cp = st.number_input('CP of Patient')
    trestbps = st.number_input('trestbps of Patient')
    chol = st.number_input('chol of Patient')
    fbs = st.number_input('fbs of Patient')
    restecg = st.number_input('restecg of Patient')
    thalach = st.number_input('thalach of Patient')
    exang = st.number_input('exang of Patient')
    oldpeak = st.number_input('oldpeak of Patient')
    slope = st.number_input('slope of Patient')
    ca = st.number_input('ca of Patient')
    thal = st.number_input('thal of Patient')

    diagnosis = ''
    if st.button('Heart Disease Prediction'):
        diagnosis = heartDiseasePrediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
    
    st.success(diagnosis)

if __name__ == '__main__':
    main()