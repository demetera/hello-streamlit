import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
       {"item": "What", "index": 4, "bought": True},
       {"item": "Propagate", "index": 3, "bought": True},
   ]
)
edited_df = st.data_editor(df, hide_index=True)
