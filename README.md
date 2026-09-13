# AI Student Assistance Chatbot

## Project Overview

AI Student Assistance Chatbot is an NLP-based chatbot developed to answer common student queries related to courses, fees, registration, course duration, class timings, location and contact information.

The chatbot uses Machine Learning techniques to understand the user's question, classify it into the appropriate intent and provide a relevant response.

## Features

- Greeting and basic conversation
- Course information
- Available courses
- Course fee information
- Registration and enrollment details
- Course duration
- Class and batch timings
- Institute location
- Contact information
- Goodbye responses
- Web-based chatbot interface

## Technologies Used

- Python
- Flask
- Scikit-learn
- NLP
- TF-IDF Vectorization
- Logistic Regression
- HTML
- CSS
- JavaScript
- JSON

## Machine Learning Approach

The chatbot uses an intent classification approach.

### 1. Dataset

Student questions are stored in `dataset.json`.

The dataset contains different intents such as:

- Greeting
- Courses
- Course Information
- Fees
- Registration
- Duration
- Timings
- Location
- Contact
- Goodbye

### 2. TF-IDF Vectorization

TF-IDF is used to convert the user's text into numerical features that can be understood by the Machine Learning model.

### 3. Logistic Regression

Logistic Regression is used to classify the user's question into one of the predefined intents.

### 4. Response Generation

After identifying the intent, the chatbot selects a suitable response from the corresponding intent.

## Project Structure

```text
AI-Student-Assistance-Chatbot/
│
├── app.py
├── chatbot.py
├── train.py
├── dataset.json
├── chatbot_model.pkl
├── vectorizer.pkl
├── requirements.txt
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

How to Run the Project:

Step 1: Clone the Repository
git clone https://github.com/tejasree-dev-code/AI-Student-Assistance-Chatbot.git

Step 2: Open the Project
cd AI-Student-Assistance-Chatbot

Step 3: Create a Virtual Environment
python -m venv venv

Step 4: Activate the Virtual Environment
For Windows:
venv\Scripts\activate

Step 5: Install Required Libraries
pip install -r requirements.txt

Step 6: Train the Chatbot Model
python train.py
You should see:
Chatbot model trained successfully!

Step 7: Run the Flask Application
python app.py

Step 8: Open the Chatbot
Open the following address in your browser:
http://127.0.0.1:5000

Example Queries:

The chatbot can answer questions such as:
Hi
What courses are available?
What is the course fee?
How much does the course cost?
How do I register?
What is the course duration?
What are the class timings?
Where is the institute?
What is the contact number?
Thank you

Future Enhancements:

Add more student-related intents
Improve chatbot accuracy with a larger dataset
Add voice input and output
Add database integration
Add student login functionality
Deploy the chatbot online
Add more personalized student assistance features

Conclusion:
This project demonstrates the use of Natural Language Processing and Machine Learning for building a simple student assistance chatbot. It combines an ML-based intent classification model with a Flask web application to provide an interactive chatbot experience.