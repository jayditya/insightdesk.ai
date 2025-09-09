import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

print("--- Starting Model Training from Excel Dataset ---")

try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # --- CHANGE #1: Point to the new .xlsx file ---
    excel_path = os.path.join(script_dir, 'support_data.xlsx')
    
    # --- CHANGE #2: Use the read_excel function ---
    df = pd.read_excel(excel_path)
    
    print("✅ Step 1: Successfully loaded 'support_data.xlsx'.")
except FileNotFoundError:
    print(f"❌ ERROR: 'support_data.xlsx' not found. Please run the 'create_excel_dataset.py' script first.")
    exit()

print("🔎 Column names found:", df.columns.tolist())

# The column names 'message' and 'category' match our new Excel file
X = df['message']
y = df['category']

print("\nStep 2: Converting text data to numerical vectors...")
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)
print("✅ Step 2 complete.")

print("\nStep 3: Training the new, smarter model...")
model = LogisticRegression()
model.fit(X_vectorized, y)
print("✅ Step 3 complete.")

# Save the newly trained model and vectorizer files
joblib.dump(model, os.path.join(script_dir, 'insight_model.pkl'))
joblib.dump(vectorizer, os.path.join(script_dir, 'vectorizer.pkl'))

print("\n--- ✅ SUCCESS! ---")
print("New model has been trained on the Excel data and saved successfully.")
