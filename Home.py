import streamlit as st
import os
## Page variables

MEDIA_DIR = os.path.join(os.getcwd(), 'media', 'Home') 

### Page content

st.image(os.join(MEDIA_DIR, 'img', 'CUU_negro_rocketred.png'))
st.title('NASA Space Apps Chihuahua')
