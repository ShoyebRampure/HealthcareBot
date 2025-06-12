from flask import Flask, render_template, request, jsonify
import os
import pandas as pd
import numpy as np
import pickle
from sklearn import preprocessing
import re

app = Flask(__name__)

# Paths to your models and data
decision_tree_model_path = r'model/disease_prediction_model.pkl'
svm_model_path = r'model/svm_disease_prediction_model.pkl'
training_file = os.path.join(os.path.dirname(__file__), 'Data', 'Training.csv')

# Load models and training data
with open(decision_tree_model_path, 'rb') as file:
    clf = pickle.load(file)

with open(svm_model_path, 'rb') as file:
    svm_model = pickle.load(file)

training = pd.read_csv(training_file)
cols = training.columns[:-1]

# Mapping strings to numbers
le = preprocessing.LabelEncoder()
y = le.fit_transform(training['prognosis'])

# Create symptoms dictionary
symptoms_dict = {symptom: index for index, symptom in enumerate(cols)}

# Function to check for matching symptoms
def check_pattern(symptoms_list, symptom_input):
    symptom_input = symptom_input.replace(' ', '_')
    pattern = re.compile(symptom_input)
    matches = [item for item in symptoms_list if pattern.search(item)]
    return matches

# Function to predict disease based on symptoms
def predict_disease(symptoms_list):
    input_vector = np.zeros(len(symptoms_dict))
    for symptom in symptoms_list:
        if symptom in symptoms_dict:
            input_vector[symptoms_dict[symptom]] = 1

    decision_tree_prediction = clf.predict([input_vector])[0]
    svm_prediction = svm_model.predict([input_vector])[0]

    return le.inverse_transform([decision_tree_prediction])[0], le.inverse_transform([svm_prediction])[0]

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    message = request.json['message']
    matches = check_pattern(cols, message)
    if matches:
        predicted_dt, predicted_svm = predict_disease(matches)
        response = f"Decision Tree prediction: {predicted_dt}, Visit the doctor as you have :  {predicted_svm}"
    else:
        response = "No matching symptoms found. Please try again."
    
    return jsonify({'bot_response': response})

if __name__ == '__main__':
    app.run(debug=True)
