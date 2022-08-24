import streamlit as st
import os
## Page variables

MEDIA_DIR = os.path.join(os.getcwd(), 'media', 'Home') 

### Page content

col1, mid, col2 = st.columns([1,1,10])
with col1:
    st.image(os.path.join(MEDIA_DIR, 'img', 'CUU_sticker_blanco1.png'), width=150)
with col2:
    st.title('NASA Space Apps Chihuahua')
