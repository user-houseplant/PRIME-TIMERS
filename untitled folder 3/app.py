import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="PRIME TIMERS",page_icon="PRMIE TIMERS",layout="wide")
st.sidebar.success("select a page above")

def ani(url):
 r=requests.get(url)
 if r.status_code !=200:
    return None
 return r.json()

lottie_coding=ani("https://lottie.host/f47019ee-582f-41c1-bf23-90c0df83c732/CohVkKfaYS.json")

title_font_size=60
title_font_weight = "bold"
st.markdown(f"<p style='font-size:{title_font_size}px; font-weight:{title_font_weight};'>PRIME TIMERS</p>", unsafe_allow_html=True)

container_font_size = 50

with st.container():
    st.write(f"""<div style='font-size:{container_font_size}px;'>
    Welcome to Prime Timers, a site for cool retired rovers. 
    Here you can join virtual social clubs (like book clubs, gardening clubs, art clubs, and many more) and discover local events for seniors happening around you. 
    Click your interest from the sidebar to explore more.
    </div>""", unsafe_allow_html=True)
with st.container():
    st_lottie(lottie_coding, height = 300, key='coding')

     
