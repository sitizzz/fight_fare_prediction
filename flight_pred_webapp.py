import numpy as np
import pickle
import base64
import streamlit as st

#loading the saved models
loaded_model = pickle.load(open('flight_rf.pkl', 'rb'))

#creating a function for prediction
def flight_prediction(input_data):
    #turn nested list into a single list
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
    return 'The estimated flight fare is {:,} rupees.'.format(prediction)

def main():
    
    #giving a title
    st.title('Flight Fare Prediction - India Region')
    
    #getting the input data from the user
    Airline = st.selectbox('Choose airline:',
                                ['Air India', 'GoAir', 'IndiGo', 'Jet Airways',
                                  'Jet Airways Business','Multiple Carriers',
                                  'Multiple Carriers Premium Economy','SpiceJet',
                                  'Trujet',' Vistara','Vistara Premium economy',
                                    'Air Asia'])

    Airline_dict = {'Air India':0, 'GoAir':1,'IndiGo':2, 'Jet Airways':3, 'Jet Airways Busness':4, 
                    'Multiple Carriers':5, 'Multiple Carriers Premium Economy':6,'SpiceJet':7,'Trujet':8,
                    'Vistara':9, 'Vistara Premium economy':10}    
    Airline1 = np.zeros(11, dtype=int)
    if Airline in Airline_dict:
        Airline1[Airline_dict[Airline]]=1
        Airline1 = list(Airline1)

    Source = st.selectbox('Choose departure:', ['Chennai', 'Delhi','Kolkata','Mumbai', 'Banglore'])
    Source_dict = {'Chennai':0, 'Delhi':1,'Kolkata':2,'Mumbai':3, 'Banglore':4}
    Source1 = np.zeros(5, dtype=int)
    if Source in Source_dict:
        Source1[Source_dict[Source]]=1
        Source1 = list(Source1)

    Destination = st.selectbox('Choose destination:', ['Cochin','Delhi', 'Hyderabad','Kolkata','New Delhi', 'Banglore'])
    Destination_dict = {'Cochin':0,'Delhi':1, 'Hyderabad':2,'Kolkata':3,'New Delhi':4, 'Banglore':5}
    Destination1 = np.zeros(6, dtype=int)
    if Destination in Destination_dict:
        Destination1[Destination_dict[Destination]]=1
        Destination1 = list(Destination)
    
    Total_Stops = st.selectbox('Choose number of transit:', list(range(4)))
    Journey_day = st.selectbox('Choose date of journey:', list(range(1,32)))
    Journey_month = st.selectbox('Choose month of journey:', list(range(1,13)))
    Dept_hour = st.selectbox('Choose hour of departure:', list(range(1,24)))
    
    array = np.arange(0,60,10)
    Dept_min = st.selectbox('Choose minute of departure:', list(array))
    Arrival_hour = st.selectbox('Choose hour of arrival:', list(range(1,24)))
    Arrival_min = st.selectbox('Choose minute of arrival:', list(array))
    Duration_hours = st.selectbox('Choose hour of duration:', list(range(1,24)))
    Duration_mins = st.selectbox('Choose minute of duration:', list(array))
      
    # code for prediction
    price = ''
    
    #creating a button for prediction
    if st.button('Price Prediction'):
               
        price = flight_prediction(list(Airline1) + list(Source1) + list(Destination1) +
                                   [Total_Stops, Journey_day, Journey_month, Dept_hour,
                                   Dept_min, Arrival_hour, Arrival_min,
                                   Duration_hours, Duration_mins])        
    st.success(price)    
    
    ###add about button
    if st.button("About"):
        st.text("This machine learning model is using Random Forest Regressor with 81% accuracy.")
        
    col1, col2, col3 = st.columns(3)
    
    with col1:        
        def get_base64_of_bin_file(bin_file):
            with open(bin_file, 'rb') as f:
                data = f.read()
            return base64.b64encode(data).decode()
        
        def get_img_with_href(local_img_path, target_url):
            bin_str = get_base64_of_bin_file(local_img_path)
            html_code = f'''
                <a href="{target_url}">
                    <img src="data:image/jpg;base64,{bin_str}" width="160" height="125"/>
                </a>'''
            return html_code
        
        st.markdown("**Sponsored by:**")
        jpg_html = get_img_with_href('brs_toped.jpg', 'https://www.tokopedia.com/bungarampaistore')
        
        st.markdown(jpg_html, unsafe_allow_html=True)
    
    with col3:
        st.markdown("**Empowered by:**")       
        jpg_html = get_img_with_href('symbol_logo_basic_color.jpg', 'https://en.apu.ac.jp/home/')
        
        st.markdown(jpg_html, unsafe_allow_html=True)
            
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
