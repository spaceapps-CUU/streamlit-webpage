import streamlit as st
import os
## Page variables

st.set_page_config()

MEDIA_DIR = os.path.join(os.getcwd(), 'media', 'Home') 

### Page content

col1, mid, col2 = st.columns([5,1,10])
with col1:
    st.image(os.path.join(MEDIA_DIR, 'img', 'CUU_sticker_blanco1.png'), width=150)
with col2:
    st.title('NASA Space Apps Chihuahua')

st.header('¿Qué es Space Apps?')

st.write(
    '''Space Apps es un hackathon auspiciado por la NASA que pretende generar soluciones creativas a problemas actuales.'''
    )

st.header('¿Quiénes pueden participar en Space Apps?')

st.write(
    '''Space Apps no tiene un público específico al cual esté enfocado, por lo que cualquier .'''
    )