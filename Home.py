import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ghoulam Mohamed Lemine")
    content1 = """
    Hi, I am Ghoulam ! I am a Python programmer, web developer, network engineer and teacher. 
    I have achieved a lot of training and get certified in Comptia A+, Network+, Linux, MSCE, RHSCA, CCNA, CCNP. 
    I worked in bunch of companies as network engineer. I am currently teaching information technology in EFC CENTER in Nouakchott.
    """
    st.info(content1)

content2 = """
Below you can find some of the apps I have built in Python. Fell free to contact me!
"""
st.write(content2)

col3,empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/"+row['image'])
        st.write(f"[source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[source code]({row['url']})")
