import numpy as np
import pickle
import base64
import streamlit as st

#loading the saved models
###no OHE model
loaded_model = pickle.load(open('flight_rf_noohe1.pkl', 'rb'))

#creating a function for prediction
def flight_prediction(input_data):
        
    #changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)

    return 'The estimated flight fare is {:,} rupees.'.format(int(prediction))

def main():
    
    #giving a title
    st.header('Flight Fare Prediction - Excluding Categorical Data')
    
    #getting the input data from the user 
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
        
        price = flight_prediction([Total_Stops, 
                                   Journey_day,
                                   Journey_month,
                                   Dept_hour,
                                   Dept_min, 
                                   Arrival_hour, 
                                   Arrival_min,
                                   Duration_hours, 
                                   Duration_mins])
        
    
    st.success(price)
       
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
    
    
    
    
    
    