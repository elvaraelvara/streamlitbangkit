# 🚲 **Bike Sharing** 🚲  
---

## 🌍 **Background**  

Bike-sharing systems are a modern evolution of traditional bike rentals, allowing users to rent and return bikes automatically. 🚴‍♂️💨  
Currently, over **500 bike-sharing programs** exist worldwide, comprising more than **500,000 bicycles**. These systems play a crucial role in:  

- 🏙️ **Urban mobility**  
- 🌱 **Environmental sustainability**  
- ❤️ **Public health improvement**  

Unlike other transport services (buses, subways), bike-sharing data records precise **travel duration, departure, and arrival locations**. This feature transforms bike-sharing systems into a **virtual sensor network** 🛰️ that can be leveraged for smart city insights. 🚦🏙️  

---

## 📊 **Dataset Overview**  

Bike rental demand is heavily influenced by **seasonal and environmental conditions** 🌦️.  
The dataset includes **two years (2011-2012) of historical data** from the **Capital Bikeshare system** 🚴 in Washington D.C., USA 🇺🇸.  

📌 **Data sources:**  
- 🚲 **Bike-sharing logs:** [Capital Bikeshare System Data](http://capitalbikeshare.com/system-data)  
- 🌦 **Weather data:** [Free Meteo](http://www.freemeteo.com)  

The dataset has been aggregated on both:  
- ⏳ **Hourly basis** (hour.csv) – **17,379 records**  
- 📅 **Daily basis** (day.csv) – **731 records**  

---

## 🛠️ **Associated Tasks**  

📈 **Regression:** Predict bike rental counts (hourly or daily) based on environmental and seasonal factors.  
🚨 **Event & Anomaly Detection:** Detect events that impact bike rentals (e.g., 🌀 Hurricane Sandy - "2012-10-30 Washington D.C.").  

---

## 📂 **Files**  

📜 **Dataset Files:**  
- 📖 `Readme.txt` – This document  
- ⏳ `hour.csv` – Bike rental counts on an **hourly** basis (**17,379** records)  
- 📅 `day.csv` – Bike rental counts on a **daily** basis (**731** records)  

---

## 🏷️ **Dataset Characteristics**  

Both `hour.csv` and `day.csv` share similar fields (except `hr`, which is absent in `day.csv`):  

| **Field**        | **Description** |
|------------------|---------------|
| 📌 `instant`  | Record index |
| 📅 `dteday`  | Date |
| 🍂 `season`  | Season (1: Spring 🌱, 2: Summer ☀️, 3: Fall 🍁, 4: Winter ❄️) |
| 📆 `yr`  | Year (0: 2011, 1: 2012) |
| 🗓 `mnth`  | Month (1-12) |
| ⏰ `hr`  | Hour of the day (0-23) |
| 🎉 `holiday`  | Whether the day is a holiday (Yes/No) |
| 📅 `weekday`  | Day of the week |
| 🏢 `workingday`  | Whether the day is a **working day** (1: Yes, 0: No) |
| 🌦️ `weathersit` | Weather situation: <br> 1️⃣ Clear ☀️ <br> 2️⃣ Mist 🌫 <br> 3️⃣ Light Snow ❄️ / Light Rain 🌧 <br> 4️⃣ Heavy Rain ⛈ / Snowstorm 🌨️ |
| 🌡️ `temp`  | Normalized temperature (max: 41°C) |
| 🌡️ `atemp`  | Normalized **feels-like** temperature (max: 50°C) |
| 💧 `hum`  | Normalized humidity (max: 100) |
| 🌬️ `windspeed`  | Normalized wind speed (max: 67) |
| 🚲 `casual`  | Count of **casual users** |
| 📋 `registered`  | Count of **registered users** |
| 🔢 `cnt`  | **Total bike rentals** (casual + registered) |

---

