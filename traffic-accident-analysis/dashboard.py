import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("Clean_Data.csv")

st.set_page_config(page_title="Road Accident Analysis", layout="wide")

# ---- Dark Theme Style ----
st.markdown("""
<style>
body {
    background-color:#0e1117;
}
[data-testid="stMetric"] {
    background-color:#1c1f26;
    padding:15px;
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

# ---- Title ----
st.title("🚦 Road Accident Analysis")

# ---- KPI Cards ----
col1,col2,col3,col4 = st.columns(4)

col1.metric("Total Accidents", len(df))
col2.metric("Total Injuries", df["Injuries"].sum())
col3.metric("Total Deaths", df["Deaths"].sum())
col4.metric("Average Driver Age", round(df["Driver_Age"].mean(),1))

# ---- Vehicle Type Donut Chart ----
vehicle = df["Vehicle_Type"].value_counts().reset_index()
vehicle.columns=["Vehicle","Count"]

fig1 = px.pie(
    vehicle,
    names="Vehicle",
    values="Count",
    hole=0.6,
    color_discrete_sequence=["#ff7f0e"]
)

fig1.update_layout(
    paper_bgcolor="#0e1117",
    font_color="white"
)

# ---- Accidents by Area Bar Chart ----
area = df["Area"].value_counts().reset_index()
area.columns=["Area","Accidents"]

fig2 = px.bar(
    area,
    x="Area",
    y="Accidents",
    color="Accidents",
    color_continuous_scale="Oranges"
)

fig2.update_layout(
    paper_bgcolor="#0e1117",
    plot_bgcolor="#0e1117",
    font_color="white"
)

# ---- Layout ----
colA,colB = st.columns(2)

with colA:
    st.subheader("Casualties by Vehicle Type")
    st.plotly_chart(fig1,use_container_width=True)

with colB:
    st.subheader("Accidents by Area")
    st.plotly_chart(fig2,use_container_width=True)

# ---- Driver Age Distribution ----
fig3 = px.histogram(
    df,
    x="Driver_Age",
    nbins=20,
    color_discrete_sequence=["#ff7f0e"]
)

fig3.update_layout(
    paper_bgcolor="#0e1117",
    plot_bgcolor="#0e1117",
    font_color="white"
)

st.subheader("Driver Age Distribution")
st.plotly_chart(fig3,use_container_width=True)