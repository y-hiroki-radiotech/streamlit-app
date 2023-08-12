import numpy as np
import altair as alt
import pandas as pd
import streamlit as st


st.header('st.write')

st.write('Hello, *world!* emoji')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

st.write('Below is a DataFrame', df, 'Above is a dataframe.')

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

st.markdown('Streamlit is **_really_ cool**.')
st.markdown('This text is :red[colored red], and this is **:blue[colored]** and bold')
st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")

st.header('This is a header')
st.subheader('This is a subheader')
st.caption('This is a string that explains something above.')
st.text('This is some text.')

code = """def hello():
    print('Hello, Streamlit!')
"""
st.code(code, language='python')