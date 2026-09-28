import streamlit as st

st.title(
    "F1 Aero Digital Twin"
)

st.metric(
    "Downforce",
    "4500 N"
)

st.metric(
    "Drag",
    "1200 N"
)

st.line_chart(
    [100,120,140,160]
)