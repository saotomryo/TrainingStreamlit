import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns=['lat','lon']
)
img = Image.open('test.png')
st.image(img,caption='Saotome Ryo',use_column_width=True)

st.map(df)

'''vscode/
st.area_chart(df)
st.line_chart(df)
'''

df = pd.DataFrame({
    '1列目' : [1,2,3,4],
    '2列目' : [10,20,30,40]
})

st.dataframe(df.style.highlight_max(axis=0),width=1000,height=1000)


st.table(df.style.highlight_max(axis=0))

"""

# 章
## 節
### 項

```Python
import streamlit as st
import numpy as np
import pandas as pd
```


"""
