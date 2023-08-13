import streamlit as st
import pandas as pd
import seaborn as sns
import datetime as dt
import matplotlib.pyplot as plt


st.title(':blue[SF Trees]')
st.markdown('<span style="color: red;">This is a red text!</span>', unsafe_allow_html=True)
st.markdown('<a href="https://www.google.com" target="_blank">Click here to open Google in a new tab!</a>', unsafe_allow_html=True)


st.write("This app analyses trees in San Francisco using"
         " a dataset kindly provided by sF DPW. The "
         "histogram below is filtered by tree onwner.")

trees_df = pd.read_csv('trees.csv')
trees_df['age'] = (pd.to_datetime('today') -
                   pd.to_datetime(trees_df['date'])).dt.days

owners = st.sidebar.multiselect('Tree Owner Filter', trees_df['caretaker'].unique())

graph_color = st.sidebar.color_picker('Graph Colors')

if owners:
    trees_df = trees_df[trees_df['caretaker'].isin(owners)]

df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']
col1, col2 = st.columns(2)

with col1:
    st.write('Tree by Width')
    fig_1, ax_1 = plt.subplots()
    ax_1 = sns.histplot(trees_df['dbh'], color=graph_color)
    plt.xlabel('Tree Width')
    st.pyplot(fig_1)

with col2:
    st.write('Tree by Age')
    fig_2, ax_2 = plt.subplots()
    ax_2 = sns.histplot(trees_df['age'], color=graph_color)
    plt.xlabel('Age (Days)')
    st.pyplot(fig_2)

st.write('Trees by Location')

trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
trees_df = trees_df.sample(n=1000, replace=True)
st.map(trees_df)

