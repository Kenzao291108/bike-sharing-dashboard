import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dashboard/bike_sharing_full.csv")

# Convert 'dteday' to datetime format
df['dteday'] = pd.to_datetime(df['dteday'])

# Mapping season numbers to names
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
df["season"] = df["season"].map(season_mapping)

# Pastikan urutan musim sesuai
season_order = ["Spring", "Summer", "Fall", "Winter"]
df["season"] = pd.Categorical(df["season"], categories=season_order, ordered=True)

# Dashboard Title
st.title("Bike Sharing Data Dashboard")

# Sidebar Filters
st.sidebar.header("Filter Data")

# Date range filter
date_range = st.sidebar.date_input("Pilih Rentang Tanggal:", [df['dteday'].min(), df['dteday'].max()],
                                   min_value=df['dteday'].min(), max_value=df['dteday'].max())

# Season filter with "All Season" option
season_options = ["All Season"] + list(df["season"].unique())
season = st.sidebar.selectbox("Pilih Musim:", season_options)

# Filter data berdasarkan rentang tanggal
filtered_df = df[(df['dteday'] >= pd.Timestamp(date_range[0])) & (df['dteday'] <= pd.Timestamp(date_range[1]))]

# Visualisasi jumlah penggunaan sepeda berdasarkan musim
st.subheader("Penggunaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(10, 6))  # Perbesar grafik

if season == "All Season":
    # Grouping data untuk semua musim
    season_counts = filtered_df.groupby("season", observed=True)["cnt"].sum().reset_index()
    sns.barplot(x="season", y="cnt", data=season_counts, order=season_order, ci=None, ax=ax, palette="Blues")

    # Menambahkan nilai di atas setiap batang
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='bottom', fontsize=12, color='black', fontweight='bold')
else:
    # Jika musim tertentu dipilih, tetap tampilkan jumlah totalnya
    season_total = filtered_df.groupby("season", observed=True)["cnt"].sum().reset_index()
    sns.barplot(x="season", y="cnt", data=season_total[season_total["season"] == season], 
                order=season_order, ci=None, ax=ax, palette="Blues")

    # Menambahkan nilai di atas batang
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='bottom', fontsize=12, color='black', fontweight='bold')

ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Penggunaan")
st.pyplot(fig)

# Visualisasi hubungan antara suhu dan jumlah pengguna
st.subheader("Hubungan Temperatur dan Jumlah Pengguna")
fig, ax = plt.subplots(figsize=(10, 6))  # Perbesar grafik
sns.scatterplot(x=filtered_df["temp"], y=filtered_df["cnt"], alpha=0.5, ax=ax)
ax.set_xlabel("Temperatur")
ax.set_ylabel("Jumlah Penggunaan")
st.pyplot(fig)

# Insight
st.subheader("Insight")
st.write("1. Penggunaan sepeda meningkat pada musim panas dan menurun di musim dingin.")
st.write("2. Terdapat korelasi positif antara suhu dan jumlah penggunaan sepeda.")
