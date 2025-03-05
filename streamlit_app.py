import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(10, 2), columns=["a", "b"])

st.bar_chart(chart_data)
