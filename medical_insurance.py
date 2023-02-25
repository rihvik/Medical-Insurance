# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 13:12:18 2023

@author: matta
"""

import pickle
import numpy as np
import streamlit as st
#load the model
loaded_model = pickle.load(open("medical_insurance.sav",'rb'))
def medical_insurance(input_data):
    input_data_as_np_array = np.asarray(input_data)
    input_data_reshape = input_data_as_np_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshape)
    print(prediction)
    return prediction
    
    
def main():
    st.title("Medical Insurance")
    age = st.text_input('Age')
    sex = st.text_input('Sex (1->Male, 0->Female)')
    
    bmi = st.text_input('BMI')
    
    smoker = st.text_input('Smoker (1->Yes, 0->No)')
    
    children = st.text_input('No of Children')
    region = st.text_input('0 = North east; 1 = North West 2 = South East; 3 = South West')
    #available for prediction
    Insurance = ''
    if st.button('Medical Insurance Amount:'):
        Insurance = medical_insurance([age,sex,bmi,smoker,region,children])
   
    st.success(Insurance)
if __name__ == '__main__':
    main()
