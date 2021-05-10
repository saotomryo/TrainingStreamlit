import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')
st.write('Interactive Widgets')

left_column,right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ回答1')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ回答2')

#option = st.text_input('あなたの趣味を教えてください')

#'あなたの趣味は',option,'です'

#condition = st.slider('あなたの今の調子は?',0,100,50)
#'コンディション：',condition



