# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:42:12 2023

@author: shiro
"""
import numpy as np
import pickle
import streamlit as st

#loading the saved models
loaded_model = pickle.load(open('C:/Users/shiro/DS exercise/end to end project/flight fare prediction/flight_rf_noohe1.pkl', 'rb'))

#creating a function for prediction
def flight_prediction(input_data):
    #changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    return 'The estimated flight fare is {} rupees.'.format(int(prediction))

def main():
    
    #giving a title
    st.title('Flight Fare Prediction Web App')
    
    #getting the input data from the user
    Total_Stops = st.selectbox('Number of stops',
                               [0,1,2,3])
    Journey_day = st.selectbox('Date of journey',
                               [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31])
    Journey_month = st.selectbox('Month of journey',
                                 [1,2,3,4,5,6,7,8,9,10,11,12])
    Dept_hour = st.selectbox('Depart (hour)',
                             [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
    Dept_min = st.selectbox('Depart (minute)',
                            [0,10,20,30,40,50])
    Arrival_hour = st.selectbox('Arrival (hour)',
                                [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
    Arrival_min = st.selectbox('Arrival (minute)',
                               [0,10,20,30,40,50])
    Duration_hours = st.selectbox('Duration (hour)',
                                  [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
    Duration_mins = st.selectbox('Duration (minute)',
                                 [0,10,20,30,40,50])
    
    # code for prediction
    price = ''
    
    #creating a button for prediction
    if st.button('Price Prediction'):
        price = flight_prediction([Total_Stops, Journey_day, Journey_month, 
                                   Dept_hour, Dept_min, Arrival_hour, 
                                   Arrival_min, Duration_hours, Duration_mins])
    
    st.success(price)
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    