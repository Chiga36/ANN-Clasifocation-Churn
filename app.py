import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler,LabelEncoder,OneHotEncoder
import pandas as pd
import pickle

## load the trained model
model = tf.keras.models.load_model('model.h5')

with open('one_hot_encode_geo.pkl','rb') as file:
    one_hot_encode_geo = pickle.load(file)
with open('label_encoder_gender.pkl','rb') as file:
    label_encoder_gender = pickle.load(file)
with open('scalar.pkl','rb') as file:
    scalar = pickle.load(file)

## Streamlit app
st.title("Customer Churn prediction")

## User input
geography = st.selectbox('Geography',one_hot_encode_geo.categories_[0])
gender = st.selectbox('Gender',label_encoder_gender.classes_)
age = st.slider('Age',18,92)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure',0,10)
num_of_products = st.slider('Number of Products',1,4)
has_cr_card = st.selectbox('Has Credit Card',[0,1])
is_active_member = st.selectbox('Is Active Member',[0,1])

## Example input data
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts':[num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
})

geo_encoded = one_hot_encode_geo.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded,columns = one_hot_encode_geo.get_feature_names_out(['Geography']))

## concatination one hot encoded
input_data = pd.concat([input_data.reset_index(drop = True),geo_encoded_df],axis=1)

input_data_scaled = scalar.transform(input_data)

predict = model.predict(input_data_scaled)
pridict_proba = predict[0][0]

st.write(f'Churn Probablity: {pridict_proba:.2f}')

if pridict_proba>0.5:
    st.write("The customer is likely to churn")
else:
    st.write("The customer is not likely to churn")