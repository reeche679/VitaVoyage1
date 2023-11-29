import streamlit as st
from PIL import Image

with st.container():
    st.title('VitVoyage.Corp')
    st.write('---')
    st.write('##')

    _, col2, _ = st.columns([1, 2, 1])
    with col2:
        st.header('Meet the Team')
        st.write('##')

    _, image_column, text_column = st.columns((1, 2, 3))
        
    with image_column:
        image = Image.open('Images/rich.jpg')
        st.image(image, width=150)
        st.write(" ")
        image = Image.open('Images/jorgette.jpg')
        st.image(image, width=150)
        st.write(" ")
        image = Image.open('Images/joriel.jpg')
        st.image(image, width=150)
        st.write(" ")
        image = Image.open('Images/kyle.jpg')
        st.image(image, width=150)
        st.write(" ")
        image = Image.open('Images/kyle.jpg')
        st.image(image, width=150)

    with text_column:
        st.write("Richmond S. Lingal - **Team Leader**")
        st.caption("Email : lingalrichmond74@gmail.com")
        st.caption("Contact Number : 0916-289-3614")
        st.divider()
        st.write("Jorgette Aira M. Amaro - **Senior Associate**")
        st.caption("Email : jorgetteairaamaro@gamil.com")
        st.caption("Contact Number : 0947-584-7075")
        st.divider()
        st.write("Joriel Laurence S. Singh - **Junior Associate**")
        st.caption("Email : jorielsingh0820@gmail.com")
        st.caption("Contact Number : 0948-570-7761")
        st.divider()
        st.write("Kyle Dranmay Dalangin - **Contributor**")
        st.caption("Email : dranmaykyle06@gmail.com")
        st.caption("Contact Number : 09465684105")
        st.divider()       
        st.write("Clarence Adrian M. Caraig - **Contributor**")
        st.caption("Email : N/A")
        st.caption("Contact Number : N/A")
        st.divider()
   

expander = st.expander("Click for more Information")

expander.write('Contacts')