import streamlit as st
st.title('Inuwa Mobarak Abraham') #setting title

html_text2 = '<hr>'
    st.markdown(html_text2, unsafe_allow_html=True)
    
    st.write('This is a prototype for predicting employee attrition using machine learning and also using cloud infrastructure')
    st.subheader('(Please fill in the Employee details accordingly)')


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
