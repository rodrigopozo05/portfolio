import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("crime_data.csv")

st.set_page_config(page_title="Crime & Safety Dashboard", layout="wide")
st.title("📊 Crime & Safety Dashboard")
st.markdown("An interactive analysis of crime data across U.S. cities.")

# KPIs
total_cities = df["City"].nunique()
total_records = len(df)
total_violent = df.shape[0]  # cada fila es un incidente
total_victims = df["Victim Count"].sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Cities Analyzed", total_cities)
col2.metric("Total Records", f"{total_records:,}")
col3.metric("Total Incidents", f"{total_violent:,}")
col4.metric("Victim Count Total", f"{total_victims:,}")

st.markdown("---")

# Top 10 cities with highest incidents
st.subheader("🔝 Top 10 Cities with Highest Incidents")
top_cities = df["City"].value_counts().head(10).reset_index()
top_cities.columns = ["City", "Incident Count"]

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x="Incident Count", y="City", data=top_cities, ax=ax, palette="Reds_r")
ax.set_title("Top 10 Cities by Number of Incidents")
st.pyplot(fig)

# Scatter plot: Victim Count vs Perpetrator Count (Top 10 States)
st.subheader("📈 Victim Count vs Perpetrator Count (Top 10 States)")

# Top 10 states por número de incidentes
top_states = df["State"].value_counts().head(10).index
df_top = df[df["State"].isin(top_states)]

# Agregamos por estado (sumando Victim y Perpetrator Count)
df_agg = df_top.groupby("State")[["Victim Count", "Perpetrator Count"]].sum().reset_index()

fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(
    x="Victim Count",
    y="Perpetrator Count",
    hue="State",
    data=df_agg,
    s=200,  # tamaño de los puntos
    palette="tab10"
)

# No se añaden nombres al lado de los puntos
ax.set_title("Victim Count vs Perpetrator Count (Top 10 States)")
st.pyplot(fig)

# Incidents per State (Top 10)
st.subheader("📊 Top 10 States by Incidents")
state_counts = df["State"].value_counts().head(10).reset_index()
state_counts.columns = ["State", "Incident Count"]

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x="Incident Count", y="State", data=state_counts, ax=ax, palette="Blues_r")
ax.set_title("Top 10 States by Number of Incidents")
plt.tight_layout()
st.pyplot(fig)

st.markdown("---")
st.markdown("👨‍💻 Developed as a **portfolio project** using Streamlit.")
