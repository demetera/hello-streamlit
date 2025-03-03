import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
       {"item": "Item 1", "index": 4, "bought": True},
       {"item": "Item 2", "index": 3, "bought": True},
   ]
)
edited_df = st.data_editor(df, hide_index=True)
