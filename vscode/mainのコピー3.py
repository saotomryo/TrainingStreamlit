import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')
st.sidebar.write('Interactive Widgets')

option = st.sidebar.text_input('あなたの趣味を教えてください')

'あなたの趣味は',option,'です'

condition = st.sidebar.slider('あなたの今の調子は?',0,100,50)
'コンディション：',condition



