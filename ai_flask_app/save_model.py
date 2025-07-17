# save_model.py (run this once to generate model.pkl & vectorizer.pkl)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Sample data
X = [
    "How do I reset my password?",
    "What are your working hours?",
    "Where is my order?",
    "Help! I can’t log in.",
    "How to cancel my subscription?"
]
y = [
    "To reset your password, click on 'Forgot Password' at login.",
    "Our working hours are 9 AM to 5 PM, Monday to Friday.",
    "You can track your order from the dashboard.",
    "Please try resetting your password first.",
    "Go to billing settings to cancel your subscription."
]

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vec, y)

# Save
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
