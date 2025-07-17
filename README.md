# 🏠 Smart Home Firebase Dashboard

This project monitors live sensor data (temperature, humidity, motion, light, energy) across 5 rooms using Firebase + Streamlit.

## 📦 Features
- Realtime dashboard from Firebase Realtime DB
- View metrics for: Bedroom1, Bedroom2, Kitchen, LivingRoom, StoreRoom
- Data upload simulation via Python

## 🚀 Usage
1. Update `firebase_secrets.py` with your Firebase Realtime DB URL
2. Run `send_sample_data.py` to simulate ESP32 sensor input
3. Launch dashboard: `streamlit run streamlit_dashboard.py`

---
🔐 Licensed under MIT License
