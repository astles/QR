import streamlit as st
from multiapp import MultiApp
from apps import home, data, model # import your app modules here

app = MultiApp()


st.set_page_config(page_title="Streamlit projects", page_icon=None, layout="centered", initial_sidebar_state="expanded", menu_items=None)

st.header("QR CODE MAKER")
st.info("Make QRs for Devices, & Users")
st.image("https://media.giphy.com/media/16dIgjWQjikY8/giphy.gif")

col1, col2 = st.columns(2)

