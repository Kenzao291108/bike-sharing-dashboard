import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("bike_sharing_full.csv")

# Dashboard Title
st.title("Bike Sharing Data Dashboard")

# Sidebar Filter
season = st.sidebar.selectbox("Pilih Musim:", df["season"].unique())
filtered_df = df[df["season"] == season]

# Visualisasi jumlah penggunaan sepeda berdasarkan musim
st.subheader("Penggunaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots()
sns.barplot(x=df["season"], y=df["cnt"], ci=None, ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Penggunaan")
st.pyplot(fig)

# Visualisasi hubungan antara suhu dan jumlah pengguna
st.subheader("Hubungan Temperatur dan Jumlah Pengguna")
fig, ax = plt.subplots()
sns.scatterplot(x=df["temp"], y=df["cnt"], alpha=0.5, ax=ax)
ax.set_xlabel("Temperatur")
ax.set_ylabel("Jumlah Penggunaan")
st.pyplot(fig)

# Insight
st.subheader("Insight")
st.write("1. Penggunaan sepeda meningkat pada musim panas dan menurun di musim dingin.")
st.write("2. Terdapat korelasi positif antara suhu dan jumlah penggunaan sepeda.")

