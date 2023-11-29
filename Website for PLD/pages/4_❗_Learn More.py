import streamlit as st
from PIL import Image

img = Image.open("398509074_359643179887697_4288406788630142671_n-removebg-preview.png")
st.set_page_config(page_title="VitaVoyage!", page_icon = img , layout="wide")


with st.container():
    left_column, right_column, middle_column = st.columns(3)
    st.header("What is VitaVoyage all about?")
    st.write("blalaalbalblablablalalblablalbalbla")