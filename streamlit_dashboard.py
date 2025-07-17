
import streamlit as st
import requests
from firebase_secrets import FIREBASE_URL

st.set_page_config(page_title="Smart Home Realtime Dashboard", layout="wide")

st.title("🏠 Smart Home Realtime Firebase Dashboard")

rooms = ["Bedroom1", "Bedroom2", "Kitchen", "LivingRoom", "StoreRoom"]
selected_room = st.selectbox("Select Room", rooms)

url = f"{FIREBASE_URL}/{selected_room}.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if data:
        st.metric("🌡️ Temperature (°C)", data.get("temperature", "N/A"))
        st.metric("💧 Humidity (%)", data.get("humidity", "N/A"))
        st.metric("🕵️ Motion Detected", str(data.get("motion", "N/A")))
        st.metric("💡 Light (LUX)", data.get("light", "N/A"))
        st.metric("⚡ Energy (kWh)", data.get("energy", "N/A"))
    else:
        st.warning("No data available for this room.")
else:
    st.error("Failed to fetch data from Firebase.")
