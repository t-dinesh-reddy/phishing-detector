# 📧 AI-Powered Phishing Email Detector with Gmail Integration

This project is a **Streamlit web app** that uses **machine learning** to detect whether an email is a phishing attempt or legitimate. It now supports **real-time Gmail inbox integration** to automatically scan unread emails for threats using AI.

---

## 🚀 Features

- 🔍 Classifies emails as **phishing** or **legitimate**
- 📊 Displays **confidence score** for predictions
- 📥 Connects to your **Gmail inbox using IMAP**
- ⚠️ Checks **unread emails** for phishing content
- ✅ Simple and fast Streamlit UI

---

## 🛠️ Tech Stack

- Python
- Streamlit
- scikit-learn
- pandas, numpy, nltk
- IMAP (via `imaplib`)
- `python-dotenv` for secure email credentials

---

## 📂 Project Structure

```
phishing-detector/
│
├── app.py                  # Streamlit UI
├── train_model.py          # ML training script
├── email_reader.py         # Gmail email fetch and analysis
├── phishing_model.pkl      # Trained ML model
├── emails.csv              # Sample dataset (optional)
├── .env                    # Stores Gmail credentials (not committed)
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```

---

## 💻 Local Setup Instructions

### ✅ Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/phishing-detector.git
cd phishing-detector
```

---

### ✅ Step 2: Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
```

---

### ✅ Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### ✅ Step 4: Set Up Gmail App Password

> Gmail requires you to use **App Passwords** for IMAP access.

1. Go to [https://myaccount.google.com/security](https://myaccount.google.com/security)
2. Enable **2-Step Verification**
3. Generate a new **App Password** under “App passwords”
4. Choose “Mail” > “Other” and name it `Phishing Detector`
5. Copy the 16-character password Google provides

---

### ✅ Step 5: Create a `.env` File

Create a file named `.env` in the root folder with:

```
EMAIL=your-email@gmail.com
EMAIL_PASS=your-16-char-app-password
```

> **Never share this file or push it to GitHub!**

---

### ✅ Step 6: Run the App

```bash
streamlit run app.py
```

The app will open in your browser at:  
`http://localhost:8501`

---

## 🌐 Optional: Deploy to Streamlit Cloud

1. Push your project to a **public GitHub repo**
2. Go to [https://share.streamlit.io](https://share.streamlit.io)
3. Link your GitHub account and select the repo
4. Deploy `app.py` as the entry point
5. **Use Streamlit secrets** to store `EMAIL` and `EMAIL_PASS` instead of `.env`

In `.streamlit/secrets.toml`:

```toml
EMAIL = "your-email@gmail.com"
EMAIL_PASS = "your-app-password"
```

In code:

```python
import streamlit as st
EMAIL = st.secrets["EMAIL"]
PASSWORD = st.secrets["EMAIL_PASS"]
```

---

## 🧠 Notes

- Basic model trained with Naive Bayes and TF-IDF
- Easily extendable to use advanced NLP (e.g., BERT)
- Add logging, database storage, or real-time alerts

---

## 🙌 Contributing

Pull requests are welcome! Fork the repo, make changes, and submit a PR.

---

## 📄 License

This project is licensed under the MIT License.

---

## 📬 Contact

Created by [Your Name](https://github.com/YOUR-USERNAME)  
For questions, collaborations, or feature requests, feel free to reach out.
