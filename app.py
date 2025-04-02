import streamlit as st
import joblib

# Load the trained model
model = joblib.load("phishing_model.pkl")

# Streamlit UI
st.title("📧 Phishing Email Detector")
st.markdown("Enter the subject or body of an email to check if it might be phishing.")

user_input = st.text_area("Enter email content here:")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        prediction = model.predict([user_input])[0]
        prob = model.predict_proba([user_input])[0]

        if prediction == 1:
            st.error("⚠️ This email is likely a **phishing attempt**.")
        else:
            st.success("✅ This email appears to be **legitimate**.")
        
        st.markdown(f"**Confidence:** {prob[prediction]:.2f}")

