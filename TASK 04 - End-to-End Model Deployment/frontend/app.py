# frontend/app.py

import streamlit as st
import requests

st.set_page_config(page_title="Personality Prediction Tool", page_icon="🧠", layout="centered")

st.markdown("<h1 style='text-align: center; color: #1f4e79;'>Personality Type Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Please provide your personal and behavioral information below to get a prediction of your personality type.</p>", unsafe_allow_html=True)
st.markdown("---")

# Input fields
name = st.text_input("Full Name", placeholder="Enter your name")

time_alone = st.slider("Average Time Spent Alone (hours per day)", 0.0, 24.0, 3.0)
stage_fear = st.radio("Do you experience stage fear?", ["Yes", "No"])
social_events = st.slider("Monthly Social Event Attendance", 0.0, 20.0, 4.0)
going_out = st.slider("Weekly Outdoor Frequency", 0.0, 7.0, 3.0)
drained = st.radio("Do you feel drained after socializing?", ["Yes", "No"])
friends = st.slider("Number of Close Friends", 0.0, 100.0, 10.0)
posts = st.slider("Monthly Social Media Post Frequency", 0.0, 30.0, 5.0)

# Submit button
if st.button("Generate Prediction"):
    if name.strip() == "":
        st.warning("Please enter your name.")
    else:
        # Prepare payload
        payload = {
            "Time_spent_Alone": time_alone,
            "Stage_fear": 1 if stage_fear == "Yes" else 0,
            "Social_event_attendance": social_events,
            "Going_outside": going_out,
            "Drained_after_socializing": 1 if drained == "Yes" else 0,
            "Friends_circle_size": friends,
            "Post_frequency": posts
        }

        try:
            response = requests.post("http://127.0.0.1:8000/predict", json=payload)

            if response.status_code == 200:
                personality = response.json()["personality_type"]
                st.success(f"Hello {name}, based on the data provided, your predicted personality type is: **{personality}**.")
            else:
                st.error("Prediction failed. Please try again later or check the backend service.")
        except Exception as e:
            st.error(f"Connection error: {e}")
