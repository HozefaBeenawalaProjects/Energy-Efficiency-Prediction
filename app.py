import streamlit as st
import numpy as np
import pickle
import pandas as pd
from PIL import Image

pickle_in1 = open('heating_load.pkl','rb')
regressor1 = pickle.load(pickle_in1)

pickle_in2 = open('cooling_load.pkl','rb')
regressor2 = pickle.load(pickle_in2)

def welcome():
    return "Welcome All"

def predict_Heating_load (Relative_compactness, Surface_area, Wall_area, Roof_area, Overall_height, Orientation, Glazing_area, Glazing_area_distribution):
    prediction=regressor1.predict ([[Relative_compactness, Surface_area, Wall_area, Roof_area, Overall_height, Orientation, Glazing_area, Glazing_area_distribution]])
    print(prediction)
    return prediction

def predict_Cooling_load (Relative_compactness, Surface_area, Wall_area, Roof_area, Overall_height, Orientation, Glazing_area, Glazing_area_distribution):
    prediction=regressor2.predict ([[Relative_compactness, Surface_area, Wall_area, Roof_area, Overall_height, Orientation, Glazing_area, Glazing_area_distribution]])
    print(prediction)
    return prediction

def main():
    st.title("Energy Efficiency prediction ML App")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Energy Efficiency Prediction</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Relative_compactness = st.text_input("Relative_compactness")
    Surface_area = st.text_input("Surface_area")
    Wall_area = st.text_input("Wall_area")
    Roof_area = st.text_input("Roof_area")
    Overall_height = st.text_input("Overall_height")
    Orientation = st.text_input("Orientation")
    Glazing_area = st.text_input("Glazing_area")
    Glazing_area_distribution = st.text_input("Glazing_area_distribution")
    result1 = ""
    result2 = ""
    if st.button("Predict Heating load"):
        result1=predict_Heating_load (Relative_compactness, Surface_area, Wall_area, Roof_area, Overall_height, Orientation, Glazing_area, Glazing_area_distribution)
    st.success('The output is {}'.format(result1))
    if st.button("Predict Cooling load"):
        result2=predict_Cooling_load (Relative_compactness, Surface_area, Wall_area, Roof_area, Overall_height, Orientation, Glazing_area, Glazing_area_distribution)
    st.success('The output is {}'.format(result2))
    if st.button("About"):
        st.text("This is a Energy Efficiency Prediction app which is used to predict heating load and cooling load requirements of buildings.")

if __name__=='__main__' :
    main()