import streamlit as st
from datetime import time, datetime


st.header('st.slider')

st.subheader('Slider')
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')


st.subheader('Range slider')
values = st.slider(
    'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# example 3
st.subheader('Range time slider')
appointment = st.slider(
    'schedule your appointment:',
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# example4
st.subheader('Datatime slider')
start_time = st.slider(
    'When do you start?',
    value=datetime(2020, 1, 1, 9, 30),
    format='MM/DD/YY - hh:mm')
st.write('Start time:', start_time)