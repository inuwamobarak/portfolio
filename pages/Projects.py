import streamlit as st

#setting title
st.title('Inuwa Mobarak Abraham')

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Asphalt Pavement Degradation")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("Colombian Fake Banknotes Detection")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("Employee Attrition Prediction")
   st.image("https://static.streamlit.io/examples/owl.jpg")


#next coloumns below

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Asphalt Pavement Degradation")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("Colombian Fake Banknotes Detection")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("Employee Attrition Prediction")
   st.image("https://static.streamlit.io/examples/owl.jpg")
