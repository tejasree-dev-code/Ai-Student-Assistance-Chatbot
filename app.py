from flask import Flask, render_template, request, jsonify
import json
import pickle
import random

app = Flask(__name__)


# Load the trained model
with open("chatbot_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load the TF-IDF vectorizer
with open("vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

# Load the chatbot dataset
with open("dataset.json", "r") as file:
    data = json.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    user_input = request.json["message"]

    # Convert user input into TF-IDF features
    user_input_vector = vectorizer.transform([user_input])

    # Predict the intent
    predicted_intent = model.predict(user_input_vector)[0]

    # Find a response
    for intent in data["intents"]:
        if intent["tag"] == predicted_intent:
            response = random.choice(intent["responses"])
            return jsonify({"response": response})

    return jsonify({"response": "Sorry, I don't understand your question."})


if __name__ == "__main__":
    app.run(debug=True)