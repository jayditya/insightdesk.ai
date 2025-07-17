import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import os

# Load dataset
df = pd.read_csv("support_data.csv")
X = df['message']
y = df['response']

# Vectorizer and model training
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vec, y)

# ✅ Create ml_model folder if it doesn't exist
os.makedirs("ml_model", exist_ok=True)

# ✅ Save model and vectorizer as .pkl files
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)
