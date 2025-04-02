import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

# Download NLTK stopwords
nltk.download('stopwords')

# Load the dataset
df = pd.read_csv("emails.csv")

# Display first few rows and column names (optional for debugging)
# print(df.head())
# print(df.columns)

# Use 'spam' column directly (already contains 0 and 1)
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['spam'], test_size=0.2, random_state=42)

# Create and train the model pipeline
model = make_pipeline(TfidfVectorizer(stop_words='english'), MultinomialNB())
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'phishing_model.pkl')

# Evaluate the model
print("Model trained. Accuracy on test set:", model.score(X_test, y_test))
