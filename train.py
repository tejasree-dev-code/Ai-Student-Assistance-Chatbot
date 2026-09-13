import json
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# Load the dataset
with open("dataset.json", "r") as file:
    data = json.load(file)


sentences = []
labels = []


# Prepare training data
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        sentences.append(pattern)
        labels.append(intent["tag"])


# Convert text into numerical features
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(sentences)


# Train the machine learning model
model = LogisticRegression()

model.fit(X, labels)


# Save the trained model
with open("chatbot_model.pkl", "wb") as file:
    pickle.dump(model, file)


# Save the TF-IDF vectorizer
with open("vectorizer.pkl", "wb") as file:
    pickle.dump(vectorizer, file)


print("Chatbot model trained successfully!")