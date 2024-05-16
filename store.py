import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
@st.cache(allow_output_mutation=True)
def load_model():
    return joblib.load('store_sale_predictionss.pkl')

# Main function to run the app
def main():
    st.title('Store Sales Prediction')
    # Load the pre-trained model
    model = load_model()
    
    # Prediction form
    st.subheader('Make a Prediction')
    item_visibility = st.number_input('Item Visibility', min_value=0.0)
    item_weight = st.number_input('Item Weight', min_value=0.0)
    item_mrp = st.number_input('Item MRP', min_value=0.0)
    Item_Fat_Content = st.number_input('Item_Fat_Content', min_value=0)
    item_Type = st.number_input('Item_Type', min_value=0.0)
    Outlet_Establishment_Year = st.number_input('Outlet_Establishment_Year', min_value=0.0)
    Outlet_Size= st.number_input('Outlet_Size', min_value=0.0)
    Outlet_Location_Type = st.number_input('Outlet_Location_Type', min_value=0.0)
    Outlet_Type= st.number_input('Outlet_Type', min_value=0.0)

  


    
    if st.button('Predict'):
        prediction = model.predict([[item_visibility, item_weight, item_mrp,Item_Fat_Content ,item_Type , Outlet_Establishment_Year,Outlet_Size, Outlet_Location_Type ,Outlet_Type]])
        st.success(f'Predicted Sales: {prediction[0]}')

if __name__ == '__main__':
    main()
