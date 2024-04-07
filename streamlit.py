import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
hour_data = pd.read_csv('hour.csv')  # Gantilah 'hour.csv' dengan nama file yang sesuai

# Streamlit App
st.set_page_config(layout="wide")
st.title('Dashboard Analisis Sewa Sepeda')

# Menu untuk memilih visualisasi
visualization_choice = st.sidebar.selectbox("Pilih Visualisasi", ["Jumlah Entri untuk Setiap Musim", 
                                                                 "Tren Jumlah Sewa Sepeda Selama Hari Libur pada Musim Panas", 
                                                                 "Perbandingan Jumlah Sewa Sepeda Selama Liburan Natal dan Tahun Baru",
                                                                 "Pengaruh Suhu dan Kelembaban terhadap Jumlah Sewa Sepeda di Akhir Pekan"])

if visualization_choice == "Jumlah Entri untuk Setiap Musim":
    # Calculate counts for each season
    spring_count = hour_data[hour_data['season'] == 1].shape[0]
    summer_count = hour_data[hour_data['season'] == 2].shape[0]
    fall_count = hour_data[hour_data['season'] == 3].shape[0]
    winter_count = hour_data[hour_data['season'] == 4].shape[0]

    # Create bar plot
    season_counts = [spring_count, summer_count, fall_count, winter_count]
    season_labels = ['Spring', 'Summer', 'Fall', 'Winter']

    plt.figure(figsize=(8, 6))
    plt.bar(season_labels, season_counts, color='skyblue')
    plt.title('Jumlah Entri untuk Setiap Musim')
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Entri')

    # Display plot in Streamlit app
    st.pyplot(plt)

    # Display counts with a nicer layout
    st.header('Jumlah Entri untuk Setiap Musim')
    st.write("Musim Semi:", spring_count)
    st.write("Musim Panas:", summer_count)
    st.write("Musim Gugur:", fall_count)
    st.write("Musim Dingin:", winter_count)

elif visualization_choice == "Tren Jumlah Sewa Sepeda Selama Hari Libur pada Musim Panas":
    # Load data
    day_data = pd.read_csv('day.csv')  # Gantilah 'day.csv' dengan nama file yang sesuai

    # Filter data for summer season
    summer_data = day_data[(day_data['season'] == 2)]

    # Separate holiday and working day data for summer season
    holiday_data = summer_data[summer_data['holiday'] == 1]
    workingday_data = summer_data[summer_data['holiday'] == 0]

    # Calculate average rentals for holiday and working days
    avg_rentals_holiday = holiday_data['cnt'].mean()
    avg_rentals_workingday = workingday_data['cnt'].mean()

    # Determine trend
    if avg_rentals_holiday > avg_rentals_workingday:
        trend = "peningkatan"
    elif avg_rentals_holiday < avg_rentals_workingday:
        trend = "penurunan"
    else:
        trend = "tidak ada perubahan"

    # Plotting
    labels = ['Holiday', 'Working Day']
    avg_rentals = [avg_rentals_holiday, avg_rentals_workingday]

    plt.figure(figsize=(8, 6))
    plt.plot(labels, avg_rentals, marker='o', color='skyblue')
    plt.title('Tren Jumlah Sewa Sepeda Selama Hari Libur pada Musim Panas')
    plt.xlabel('Hari')
    plt.ylabel('Rata-rata Jumlah Sewa Sepeda')
    plt.grid(True)

    # Display plot in Streamlit app
    st.pyplot(plt)

    # Display trend in Streamlit app
    st.title('Tren Jumlah Sewa Sepeda Selama Hari Libur pada Musim Panas')
    st.write(f"Tren jumlah sewa sepeda selama hari libur pada musim panas: {trend}")

elif visualization_choice == "Perbandingan Jumlah Sewa Sepeda Selama Liburan Natal dan Tahun Baru":
    # Load data
    day_data = pd.read_csv('day.csv')  # Gantilah 'day.csv' dengan nama file yang sesuai

    # Additional analysis
    holiday_season_data = day_data[(day_data['dteday'] >= '2011-12-20') & (day_data['dteday'] <= '2012-01-05')]
    total_rentals_holiday_season = holiday_season_data['cnt'].sum()

    pre_holiday_data = day_data[(day_data['dteday'] >= '2011-12-10') & (day_data['dteday'] < '2011-12-20')]
    total_rentals_pre_holiday = pre_holiday_data['cnt'].sum()

    post_holiday_data = day_data[(day_data['dteday'] > '2012-01-05') & (day_data['dteday'] <= '2012-01-15')]
    total_rentals_post_holiday = post_holiday_data['cnt'].sum()

    if total_rentals_holiday_season > total_rentals_pre_holiday and total_rentals_holiday_season > total_rentals_post_holiday:
        trend = "peningkatan"
    elif total_rentals_holiday_season < total_rentals_pre_holiday and total_rentals_holiday_season < total_rentals_post_holiday:
        trend = "penurunan"
    else:
        trend = "tidak ada perubahan"

    total_rentals = [total_rentals_pre_holiday, total_rentals_holiday_season, total_rentals_post_holiday]
    labels = ['Sebelum Liburan', 'Liburan', 'Sesudah Liburan']
    colors = ['blue', 'green', 'orange']

    plt.figure(figsize=(10, 6))
    plt.bar(labels, total_rentals, color=colors)

    plt.title('Perbandingan Jumlah Sewa Sepeda Selama Liburan Natal dan Tahun Baru')
    plt.xlabel('Periode')
    plt.ylabel('Jumlah Sewa Sepeda Harian')

    plt.grid(axis='y')

    # Display plot in Streamlit app
    st.pyplot(plt)

    # Display trend in Streamlit app
    st.write("Trend penggunaan sepeda berbagi selama liburan Natal dan Tahun Baru:", trend)

elif visualization_choice == "Pengaruh Suhu dan Kelembaban terhadap Jumlah Sewa Sepeda di Akhir Pekan":
    # Weekend analysis
    day_data = pd.read_csv('day.csv')  # Gantilah 'day.csv' dengan nama file yang sesuai

    weekend_data = day_data[day_data['workingday'] == 0]
    temperature = weekend_data['temp']
    humidity = weekend_data['hum']
    rentals = weekend_data['cnt']

    plt.figure(figsize=(10, 6))
    plt.scatter(temperature, rentals, c=humidity, cmap='coolwarm', alpha=0.8)

    plt.title('Pengaruh Suhu dan Kelembaban terhadap Jumlah Sewa Sepeda di Akhir Pekan')
    plt.xlabel('Suhu (Celsius)')
    plt.ylabel('Jumlah Sewa Sepeda Harian')
    plt.colorbar(label='Kelembaban')

    plt.grid(True)

    # Display plot in Streamlit app
    st.pyplot(plt)
