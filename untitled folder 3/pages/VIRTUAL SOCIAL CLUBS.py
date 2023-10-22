import requests
import streamlit as st
from streamlit_lottie import st_lottie
import sqlite3

def ani(url):
 r=requests.get(url)
 if r.status_code !=200:
    return None
 return r.json()

lottie_coding=ani("https://lottie.host/3faf427b-f84e-4ab6-b67b-806e83c16df1/K9EF2CNvDS.json")


conn = sqlite3.connect('social_club.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS clubs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        schedule TEXT,
        organizer TEXT,
        members TEXT
    )
''')
conn.commit()



title_font_size=60
title_font_weight = "bold"
st.markdown(f"<p style='font-size:{title_font_size}px; font-weight:{title_font_weight};'>VIRTUAL SOCIAL CLUBS</p>", unsafe_allow_html=True)


st.markdown(
    """
    <style>
    
    body {
        font-size: 60px;
    }

   
    .stButton button {
        font-size: 50px;
    }

    
    .stButton button {
        padding: 40px 50px;
        }
    .stSelectbox label {
        font-size: 50px;
    }

    .stTextInput input {
        font-size: 70px; 
    }

   
    .stTextArea textarea {
        font-size: 70px; 
    h2 {
        font-size: 70px; 
    }
    </style>
    """,
    unsafe_allow_html=True
)


menu = st.sidebar.selectbox("Navigation", ["Home", "Create Club"], key="menu", help="Select a page")


if menu == "Home":
    with st.container():
     left_column,right_column = st.columns(2)
    with left_column:
    
      st.markdown(f"<p style='font-size:{title_font_size}px; font-weight:{title_font_weight};'>Available Clubs</p>", unsafe_allow_html=True)

    
      cursor.execute("SELECT * FROM clubs")
      clubs = cursor.fetchall()

      for club in clubs:
          st.subheader(club[1])
          st.write(f"Description: {club[2]}")
          st.write(f"Schedule: {club[3]}")
          st.write(f"Organizer: {club[4]}")
          st.write(f"Members: {club[5]}")
    with right_column:
        st_lottie(lottie_coding, height = 600, key='coding')  


if menu == "Create Club":
    title_font_size=60
    st.markdown(f"<p style='font-size:{title_font_size}px; font-weight:{title_font_weight};'>CREATE A SOCIAL CLUB</p>", unsafe_allow_html=True)

   
    st.markdown(
        """
        <style>
       
        .stTextInput input[data-baseweb="input"][data-testid="stTextInput"][placeholder="Club Name"],
        .stTextArea textarea[data-baseweb="textarea"][placeholder="Club Description"],
        .stTextArea textarea[data-baseweb="textarea"][placeholder="Club Schedule"],
        .stTextInput input[data-baseweb="input"][data-testid="stTextInput"][placeholder="Organizer"] {
            font-size: 60px; 
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <style>
        
        .stTextInput label,
        .stTextArea label {
            font-size: 60px; 
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    
    club_name = st.text_input("CLUB NAME", key="club_name")

    club_description = st.text_area("CLUB DESCRIPTION", key="club_description")


    club_schedule = st.text_area("CLUB SCHEDULE", key="club_schedule")


    club_organizer = st.text_input("ORGANIZER", key="club_organizer")

    
    if st.button("Create Club", key="create_button"):
        cursor.execute("INSERT INTO clubs (name, description, schedule, organizer, members) VALUES (?, ?, ?, ?, ?)",
                       (club_name, club_description, club_schedule, club_organizer, club_organizer))
        conn.commit()
        st.success(f"Club '{club_name}' created successfully.")


conn.close()