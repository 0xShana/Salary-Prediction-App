from types import DynamicClassAttribute
from pytz import country_timezones
import streamlit as st
import pickle
import numpy as np
def load_model():
    with open('saved_steps.pkl','rb') as file:
        data = pickle.load(file)
    return data
data = load_model()


regressor = data['model']
le_country = data['le_country']
le_education = data['le_education']

def show_predict_page():
    st.title("Software Develper Salary Prediction - Latest")
    st.write("""### Give us some details ...""")
    st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://images.pexels.com/photos/943096/pexels-photo-943096.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260")
    }
   .sidebar .sidebar-content {
        background: url("https://images.pexels.com/photos/6771985/pexels-photo-6771985.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260")
        }</style>""",unsafe_allow_html=True)
    countries=(
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russia",
        "Sweden"
        )
    education=(
        'Less than a Bachelors',
        'Bachelor’s degree',
        'Master’s degree',
        'Post grad'
    )
    country=st.selectbox("Countries ",countries)
    education=st.selectbox('Education ',education)
    experience=st.slider("Years of Experience ",0,30,5)

    ok=st.button("Calculate The Salary")

    if ok:
        X=np.array([[country,education,experience]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)
        salary = regressor.predict(X)
        st.subheader(f"The Estimated Salary is :: ${salary[0]:.2f}") 