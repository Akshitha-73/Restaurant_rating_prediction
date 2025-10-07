import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

model=pickle.load(open('model.pkl','rb'))
le_city = pickle.load(open("le_city.pkl", "rb"))

st.title('Prediction of restaurants rating')
st.set_page_config(layout='wide')
input_method = st.sidebar.radio("Choose Input Type", ["Manual Entry", "Upload file"])
if input_method=='Upload file':
    uploaded_file=st.file_uploader('Upload any file',type=['csv','xlsx'])
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"):
            data = pd.read_csv(uploaded_file)
        else:
            data = pd.read_excel(uploaded_file)
           
        columns_to_drop = [
        'Restaurant ID',
        'Restaurant Name',
        'Country Code',
        'Currency',
        'Is delivering now',
        'Switch to order menu',
        'Address',
        'Locality',
        'Locality Verbose',
        'Rating color',
        'Latitude',
        'Longitude'
        ]

        data1=data.drop(columns=columns_to_drop)
        data1['Cuisine List'] = data1['Cuisines'].apply(lambda x: [c.strip() for c in str(x).split(',')] if pd.notnull(x) else [])
        data1['Cuisine Count'] = data1['Cuisine List'].apply(len)
        data1=data1.drop(columns=['Cuisines','Cuisine List'])
        binary_cols = ['Has Table booking', 'Has Online delivery']
        for col in binary_cols:
            data1[col] = data1[col].map({'Yes': 1, 'No': 0})
        data1['City'] = le_city.transform(data1["City"])  
        rating_map = {
        "Not rated": 0,
        "Poor": 1,
        "Average": 2,
        "Good": 3,
        "Very Good": 4,
        "Excellent": 5
        }

        data1["Rating text"] = data1["Rating text"].map(rating_map)

    
        if st.button('Predict'):
            prediction=model.predict(data1) 
            st.subheader("Predicted Ratings")
            data['Prediction']=prediction
            st.write(pd.DataFrame(data))
            csv = data.to_csv(index=False).encode("utf-8")
            st.download_button("Download Results as CSV", csv, "predicted_ratings.csv", "text/csv")


elif input_method=='Manual Entry':
    st.markdown("Predict the **aggregate rating** of a restaurant based on its features.")
    
    city = st.number_input("City (encoded value)", min_value=0, step=1)
    votes = st.number_input("Number of Votes", min_value=0, step=1)
    has_table = st.selectbox("Has Table Booking?", [0, 1])
    has_online = st.selectbox("Has Online Delivery?", [0, 1])
    price_range = st.selectbox("Price Range (1=Low, 4=High)", [1, 2, 3, 4])
    cuisine_count = st.number_input("Cuisine Count", min_value=1, step=1)
    avg_cost = st.number_input("Average Cost for Two", min_value=0, step=1)
    rating_text = st.selectbox(
        "Rating Text", 
        options=[0, 1, 2, 3, 4, 5],
        format_func=lambda x: ["Not rated", "Poor", "Average", "Good", "Very Good", "Excellent"][x])
    features = np.array([[city, votes, has_table, has_online, price_range,rating_text ,avg_cost, cuisine_count]])
    if st.button("Predict Rating"):
        prediction = model.predict(features)[0]
        st.success(f"Predicted Aggregate Rating: **{prediction:.2f}**")
else:
    st.write('Please select any input mode')


