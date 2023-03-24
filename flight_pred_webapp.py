import numpy as np
import pickle
import streamlit as st

#loading the saved models
loaded_model = pickle.load(open('flight_rf.pkl', 'rb'))

#creating a function for prediction
def flight_prediction(input_data):
    #turn nested list into a single list
    print(input_data)
    new_input_data=[]
    for element in input_data:
        if type(element)==list:
            new_input_data.extend(element)
        else:
            new_input_data.append(element)
        
    #changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(new_input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    # return (prediction)
    return 'The estimated flight fare is {} rupees.'.format(int(prediction))

def main():
    
    #giving a title
    st.title('Flight Fare Prediction Web App')
    
    #getting the input data from the user
    Airline = st.selectbox('Airline',
                                ['Air India', 'GoAir', 'IndiGo', 'Jet Airways',
                                  'Jet Airways Business','Multiple Carriers',
                                  'Multiple Carriers Premium Economy','SpiceJet',
                                  'Trujet',' Vistara','Vistara Premium economy',
                                    'Air Asia'])
    if (Airline == 'Air India'):
        Airline = [1,0,0,0,0,0,0,0,0,0,0]
    elif (Airline == 'GoAir'):
        Airline = [0,1,0,0,0,0,0,0,0,0,0]
    elif (Airline=='IndiGo'):
        Airline = [0,0,1,0,0,0,0,0,0,0,0]
    elif (Airline=='Jet Airways'):
        Airline = [0,0,0,1,0,0,0,0,0,0,0]
    elif (Airline=='Jet Airways Business'):
        Airline = [0,0,0,0,1,0,0,0,0,0,0]
    elif (Airline=='Multiple Carriers'):
        Airline = [0,0,0,0,0,1,0,0,0,0,0]
    elif (Airline=='Multiple Carriers Premium Economy'):
        Airline = [0,0,0,0,0,0,1,0,0,0,0]
    elif (Airline=='SpiceJet'):
        Airline = [0,0,0,0,0,0,0,1,0,0,0]
    elif (Airline=='Trujet'):
        Airline = [0,0,0,0,0,0,0,0,1,0,0]
    elif (Airline=='Vistara'):
        Airline = [0,0,0,0,0,0,0,0,0,1,0]
    elif (Airline=='Vistara Premium economy'):
        Airline = [0,0,0,0,0,0,0,0,0,0,1]
    else:
        Airline =[0,0,0,0,0,0,0,0,0,0,0]
   
    
    Source = st.selectbox('Source',
                          ['Chennai', 'Delhi','Kolkata','Mumbai', 'Banglore'])
    if (Source == 'Chennai'):
        Source = [1,0,0,0]
    elif (Source == 'Delhi'):
        Source = [0,1,0,0] 
    elif (Source == 'Kolkata'):
        Source = [0,0,1,0]
    elif (Source == 'Mumbai'):
        Source = [0,0,0,1]
    else:
        Source = [0,0,0,0]
 

    Destination = st.selectbox('Destination',
                                ['Cochin','Delhi', 'Hyderabad','Kolkata','New Delhi', 'Banglore'])
    if (Destination == 'Cochin'):
        Destination = [1,0,0,0,0]
    elif (Destination == 'Delhi'):
        Destination = [0,1,0,0,0] 
    elif (Destination == 'Hyderabad'):
        Destination = [0,0,1,0,0]
    elif (Destination == 'Kolkata'):
        Destination = [0,0,0,1,0]
    elif (Destination == 'New Delhi'):
        Destination = [0,0,0,0,1]
    else:
        Destination = [0,0,0,0,0]
  
    
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
        
        price = flight_prediction([
            Airline, Source, Destination,
                                   Total_Stops, 
                                   Journey_day,
                                   Journey_month,
                                   Dept_hour,
                                   Dept_min, 
                                   Arrival_hour, 
                                   Arrival_min,
                                   Duration_hours, 
                                   Duration_mins])
        
    st.success(price)    
    
    ###add about button
    if st.button("About"):
        st.text("This machine learning model is using Random Forest Regressor with 81% accuracy.")
        
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    