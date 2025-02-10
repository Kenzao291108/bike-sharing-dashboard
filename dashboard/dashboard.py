import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dashboard/bike_sharing_full.csv")

# Convert 'dteday' to datetime format
df['dteday'] = pd.to_datetime(df['dteday'])

# Mapping season numbers to names
season_mapping = {1: "Springer", 2: "Summer", 3: "Fall", 4: "Winter"}
df['season'] = df['season'].map(season_mapping)

# Dashboard Title
st.title("Bike Sharing Data Dashboard")

# Sidebar Filters
st.sidebar.header("Filter Data")

# Date range filter
date_range = st.sidebar.date_input("Pilih Rentang Tanggal:", [df['dteday'].min(), df['dteday'].max()],
                                   min_value=df['dteday'].min(), max_value=df['dteday'].max())

# Season filter
season = st.sidebar.selectbox("Pilih Musim:", df["season"].unique())

# Filter data berdasarkan rentang tanggal dan musim
filtered_df = df[(df['dteday'] >= pd.Timestamp(date_range[0])) & (df['dteday'] <= pd.Timestamp(date_range[1]))]
filtered_df = filtered_df[filtered_df["season"] == season]

# Visualisasi jumlah penggunaan sepeda berdasarkan musim
st.subheader("Penggunaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots()
sns.barplot(x=filtered_df["season"], y=filtered_df["cnt"], ci=None, ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Penggunaan")
st.pyplot(fig)

# Visualisasi hubungan antara suhu dan jumlah pengguna
st.subheader("Hubungan Temperatur dan Jumlah Pengguna")
fig, ax = plt.subplots()
sns.scatterplot(x=filtered_df["temp"], y=filtered_df["cnt"], alpha=0.5, ax=ax)
ax.set_xlabel("Temperatur")
ax.set_ylabel("Jumlah Penggunaan")
st.pyplot(fig)

# Insight
st.subheader("Insight")
st.write("1. Penggunaan sepeda meningkat pada musim panas dan menurun di musim dingin.")
st.write("2. Terdapat korelasi positif antara suhu dan jumlah penggunaan sepeda.")
