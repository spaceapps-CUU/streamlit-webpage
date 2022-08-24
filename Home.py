import streamlit as st
import os
## Page variables

MEDIA_DIR = os.path.join(os.getcwd(), 'media', 'Home') 

### Page content

st.image(os.path.join(MEDIA_DIR, 'img', 'CUU_sticker_blanco1.png'), width=200)
st.title('NASA Space Apps Chihuahua')
