import streamlit as st
from streamlit_gsheets import GSheetsConnection
import random


# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()


ran = random.randint(0, len(df) - 1)
st.title(f"{df['eng'][ran]} - {df['rus'][ran]}")
