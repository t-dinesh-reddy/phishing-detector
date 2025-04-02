# 📧 AI-Powered Phishing Email Detector

This project is a **Streamlit web app** that uses **machine learning** to detect whether an email is a phishing attempt or a legitimate message. It was built to demonstrate the use of AI in cybersecurity through natural language processing and classification models.

---

## 🚀 Features

- 🔍 Classifies emails as **phishing** or **legitimate**
- 📊 Displays **confidence score** of the prediction
- 🌐 Easy-to-use **Streamlit web interface**
- 🧠 Trained using **TF-IDF + Naive Bayes** classifier
- ✅ Lightweight and quick to test locally

---

## 🛠️ Tech Stack

- **Python**
- **Scikit-learn** for machine learning
- **NLTK** for natural language processing
- **Streamlit** for the web UI
- **pandas, numpy, joblib** for data handling and model saving

---

## 📂 Project Structure

phishing-detector/
│
├── app.py                  # Your Streamlit app
├── emails.csv              # Dataset (optional for training)
├── phishing_model.pkl      # Trained ML model
├── train_model.py          # Script used to train the model
├── requirements.txt        # Python dependencies
└── README.md               # Project overview

---

## 💻 How to Clone and Run Locally

### ✅ Step 1: Clone the Repository

```bash
git clone https://github.com/t-dinesh-reddy/phishing-detector.git
cd phishing-detector

---

✅ Step 2: Set Up the Environment
If you’re using a virtual environment (recommended):
python -m venv venv
source venv/bin/activate         # On Windows: venv\Scripts\activate

---

✅ Step 3: Install Dependencies
pip install -r requirements.txt

---

✅ Step 4: Run the Streamlit App
streamlit run app.py
The app will open automatically in your browser at http://localhost:8501

---

📌 Notes
The initial model is basic and trained on a small dataset. For production use, train it with a larger phishing email dataset.
You can enhance the model using advanced NLP models (e.g., BERT).
Extend it with features like file upload for .eml, spam logging, or suspicious keyword highlighting.

---

🙌 Contributing
Pull requests are welcome! If you'd like to improve the model, UI, or add features, feel free to fork the repo and open a PR.

---

