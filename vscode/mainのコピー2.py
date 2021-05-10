import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')
st.write('Interactive Widgets')

option = st.text_input('あなたの趣味を教えてください')

'あなたの趣味は',option,'です'

condition = st.slider('あなたの今の調子は?',0,100,50)
'コンディション：',condition


'''
option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
)

'あなたの好きな数字は',option,'です'


#if st.checkbox('Show Image'):
#    img = Image.open('test.png')
#    st.image(img,caption='Saotome Ryo',use_column_width=True)
'''
