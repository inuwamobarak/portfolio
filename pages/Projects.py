import streamlit as st
import base64

#setting background
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:images/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('images/background-2462430.jpg')

#setting title
st.title('Inuwa Mobarak Abraham')
html_text2 = '<hr>'
st.markdown(html_text2, unsafe_allow_html=True)

st.subheader('Please find some of my Projects below')
st.write('Below is a compilation of some of my Data Science research and projects.')

st.header("Asphalt Pavement Degradation")
st.write('It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair')
st.image("images/engineer.jpg")

st.header("Colombian Fake Banknotes Detection")
st.image("images/bg2.jpg")

st.header("Employee Attrition Prediction")
st.image("images/rsz_bg4.png")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Asphalt Pavement Degradation")
   st.image("images/engineer.jpg")

with col2:
   st.header("Colombian Fake Banknotes Detection")
   st.image("images/bg2.jpg")

with col3:
   st.header("Employee Attrition Prediction")
   st.image("images/rsz_bg4.png")

#adding horizontal rule
html_text2a = '<hr>'
st.markdown(html_text2a, unsafe_allow_html=True)
