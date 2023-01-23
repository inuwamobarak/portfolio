import streamlit as st
import base64
from PIL import Image

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
add_bg_from_local('images/pexels-andreea-ch-1166643.jpg')

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://media.licdn.com/dms/image/D4D03AQGbIvI6rSK-MA/profile-displayphoto-shrink_200_200/0/1667341916049?e=1680134400&v=beta&t=9A0bwgTzgt2zAaH8kxA6-uu6GShheBRjf1JUESJQDFU);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "Inuwa Mobarak";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
add_logo()

#adding header image
col1, col2, col3 = st.columns([4,6,1])
with col1:
 image = Image.open('images/IMG_20221017_170620_857.jpg')
 st.image(image, caption='Inuwa Mobarak Abraham')
 #st.image('https://media.licdn.com/dms/image/D4D03AQGbIvI6rSK-MA/profile-displayphoto-shrink_200_200/0/1667341916049?e=1680134400&v=beta&t=9A0bwgTzgt2zAaH8kxA6-uu6GShheBRjf1JUESJQDFU')
    
with col2:
 st.title("Data Science Portfolio")
 st.write("According to data from the BCG-WEF project report, 72% of manufacturing organizations use advanced data analytics to boost efficiency.")
    
with col3:
 st.write("")
html_text2 = '<hr>'
st.markdown(html_text2, unsafe_allow_html=True)

st.subheader('Please find some of my Projects below')
st.write('Below is a compilation of some of my Data Science research and projects.')
html_text2 = '<hr>'
st.markdown(html_text2, unsafe_allow_html=True)

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
