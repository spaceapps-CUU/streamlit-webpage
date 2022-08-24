import streamlit as st
import os
## Page variables

MEDIA_DIR = os.path.join(os.getcwd(), 'media', 'Home') 

st.set_page_config(page_title='Space Apps CUU', page_icon=os.path.join(MEDIA_DIR, 'img', 'CUU_sticker_blanco1.png'))

### Page content

col1, mid, col2 = st.columns([5,1,10])
with col1:
    st.image(os.path.join(MEDIA_DIR, 'img', 'CUU_sticker_blanco1.png'), width=150)
with col2:
    st.title('NASA Space Apps Chihuahua')

st.header('¿Qué es Space Apps?')

st.write(
    '''Space Apps es una iniciativa de la NASA que busca reunir a las mentes más creativas del planeta para generar propuestas de solución a problemas de la Tierra y el espacio.

Durante un fin de semana, participantes alrededor de todo el mundo se organizan en equipos para resolver uno de los desafíos propuestos por la NASA y sus colaboradores.'''
    )

st.header('¿Quién puede participar en Space Apps?')

st.write(
    '''¡Space Apps es para todos! Sin importar tu edad, escolaridad y experiencia, en Space Apps eres bienvenido a integrarte a un equipo y disfrutar al máximo esta experiencia.
    
Para participantes menores de edad, es necesario presentar un formato de consentimiento de parte de sus tutores legales para poder formar parte del evento.

Los participantes menores a los 13 años deberán estar acompañados en todo momento por un tutor legal.'''
    )