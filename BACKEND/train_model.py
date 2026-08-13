import pandas as pd
import re
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# ==========================================
# 1. DATASET PATHS
# ==========================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FAKE_PATH = os.path.join(BASE_DIR, "dataset", "Fake.csv")
TRUE_PATH = os.path.join(BASE_DIR, "dataset", "True.csv")


# ==========================================
# 2. LOAD DATASET
# ==========================================

print("Loading datasets...")

fake_data = pd.read_csv(FAKE_PATH)
true_data = pd.read_csv(TRUE_PATH)

print("Fake news records:", len(fake_data))
print("Real news records:", len(true_data))


# ==========================================
# 3. ADD LABELS
# ==========================================

fake_data["label"] = 0
true_data["label"] = 1


# ==========================================
# 4. COMBINE DATA
# ==========================================

data = pd.concat([fake_data, true_data], ignore_index=True)

print("Total records:", len(data))


# ==========================================
# 5. HANDLE MISSING VALUES
# ==========================================

data["title"] = data["title"].fillna("")
data["text"] = data["text"].fillna("")


# ==========================================
# 6. COMBINE TITLE + TEXT
# ==========================================

data["content"] = data["title"] + " " + data["text"]


# ==========================================
# 7. TEXT CLEANING
# ==========================================

def clean_text(text):

    text = str(text)

    text = text.lower()

    text = re.sub(r"http\S+|www\S+|https\S+", "", text)

    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


print("Cleaning text...")

data["content"] = data["content"].apply(clean_text)


# ==========================================
# 8. FEATURES AND LABEL
# ==========================================

X = data["content"]
y = data["label"]


# ==========================================
# 9. TRAIN / TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Training records:", len(X_train))
print("Testing records:", len(X_test))


# ==========================================
# 10. TF-IDF VECTORIZATION
# ==========================================

print("Creating TF-IDF features...")

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=50000,
    ngram_range=(1, 2)
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


# ==========================================
# 11. TRAIN MODEL
# ==========================================

print("Training Logistic Regression model...")

model = LogisticRegression(
    max_iter=1000
)

model.fit(X_train_tfidf, y_train)


# ==========================================
# 12. EVALUATE MODEL
# ==========================================

y_pred = model.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, y_pred)

print("\n================================")
print("MODEL RESULTS")
print("================================")

print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=["FAKE", "REAL"]
))


# ==========================================
# 13. SAVE MODEL
# ==========================================

MODEL_PATH = os.path.join(BASE_DIR, "backend", "fake_news_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "backend", "tfidf_vectorizer.pkl")

joblib.dump(model, MODEL_PATH)
joblib.dump(vectorizer, VECTORIZER_PATH)


# ==========================================
# 14. SUCCESS MESSAGE
# ==========================================

print("\n================================")
print("TRAINING COMPLETED SUCCESSFULLY")
print("================================")

print("Model saved to:")
print(MODEL_PATH)

print("Vectorizer saved to:")
print(VECTORIZER_PATH)
