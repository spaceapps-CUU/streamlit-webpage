from atexit import register
import streamlit as st

REGISTER_OPEN = True
REGISTER_LINK = 'https://forms.gle/jFke6EwTeJmKRm5c9'

st.title('Registro de participantes')
st.header('¿Listo para el reto?')

if(REGISTER_OPEN):
    st.write('Actualmente el registro se encuentra abierto puedes registrar a tu equipo desde el siguiente link:')
    st.write(REGISTER_LINK)
