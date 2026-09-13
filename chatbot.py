import json
import pickle
import random


# Load the trained model and vectorizer
with open("chatbot_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)


# Load the chatbot dataset
with open("dataset.json", "r") as file:
    data = json.load(file)


print("AI Student Assistant is ready!")
print("Type 'quit' to stop the chatbot.")

while True:

    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Bot: Goodbye!")
        break

    # Convert user input into TF-IDF features
    user_input_vector = vectorizer.transform([user_input])

    # Predict the intent
    predicted_intent = model.predict(user_input_vector)[0]

    # Find the response for the predicted intent
    for intent in data["intents"]:
        if intent["tag"] == predicted_intent:
            response = random.choice(intent["responses"])
            print("Bot:", response)
            break