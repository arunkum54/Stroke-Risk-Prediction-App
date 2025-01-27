# I have deployed the solution, and can access it via the following link:
 https://stroke-risk-prediction-app.streamlit.app/

# Stroke Risk Prediction Application

This repository contains two implementations of a stroke risk prediction model:
1. **Streamlit App**: A web app built using Streamlit for a user-friendly interface to predict stroke risk.
2. **Flask API**: A RESTful API built using Flask that allows users to send POST requests to predict stroke risk.

## Project Structure

## Components

### 1. **best_stroke_model.pkl**
This is the pre-trained machine learning model used for stroke risk prediction. The model is created using various health-related features such as gender, age, hypertension, heart disease, and others. It is saved as a `.pkl` file, which is loaded in both the **Streamlit App** and the **Flask API** for making predictions.

### 2. **flask_app.py**
The **Flask API** serves as a backend service to predict stroke risk. It provides an endpoint (`/predict`) where users can send a **POST** request with health-related data in JSON format. The Flask API processes the input data, uses the pre-trained model (`best_stroke_model.pkl`), and returns the prediction (stroke risk) and confidence level.

- **POST Request**: The API accepts a **POST** request with a JSON body containing the following fields:
    - `gender`
    - `age`
    - `hypertension`
    - `heart_disease`
    - `ever_married`
    - `work_type`
    - `Residence_type`
    - `avg_glucose_level`
    - `bmi`
    - `smoking_status`
    - `high_blood_pressure`
  
  The API will respond with the stroke risk prediction and confidence.

- **Postman Usage**: The Flask API can be tested using Postman by sending a POST request to `http://localhost:5001/predict` with the required fields in the body.

### 3. **streamlit_app.py**
The **Streamlit App** is a user-friendly web interface that allows users to interact with the stroke prediction model. It provides input fields such as gender, age, hypertension, heart disease, and more. When the user clicks the "Predict Stroke Risk" button, the app processes the input data, makes a prediction using the model, and displays the result along with the confidence level.

- **Web-based Interface**: The app runs locally in the browser and allows users to input their health data directly into the fields.
- **Live Prediction**: As soon as the user inputs the data and clicks the button, the app provides an immediate prediction of stroke risk.

### 4. **Model_Creation.py**
This script is used for training and creating the stroke risk prediction model (`best_stroke_model.pkl`). It involves loading the dataset, preprocessing the data, and training a machine learning model (such as a logistic regression or decision tree classifier). The trained model is then saved as a `.pkl` file for use in both the **Flask API** and the **Streamlit App**.

#### Model Creation Steps:
1. **Data Collection**: The dataset is collected from various sources, which include health-related features such as age, gender, hypertension, etc.
2. **Data Preprocessing**: The data is cleaned and transformed to make it suitable for model training (e.g., encoding categorical variables, handling missing values).
3. **Model Training**: A machine learning model is trained using the preprocessed data.
4. **Model Saving**: The trained model is saved as a `.pkl` file (`best_stroke_model.pkl`), which is then used in both the Flask and Streamlit applications for making predictions.


## Installation

To run the applications locally, follow these steps:

1. **Clone the repository**:

    git clone https://github.com/arunkum54/Stroke-Risk-Prediction-App.git
    
    cd stroke-risk-prediction

2. **Create a virtual environment** (optional but recommended):
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install dependencies**:

    pip install -r requirements.txt

## Streamlit App

The Streamlit app provides an interactive UI where users can input personal details and predict stroke risk.

### Running the Streamlit App

To run the Streamlit app, use the following command:

streamlit run streamlitapp.py

This will open the app in your default web browser. The app includes the following input fields:

Gender
Age
Hypertension
Heart Disease
Ever Married
Work Type
Residence Type
Average Glucose Level
BMI
Smoking Status
High Blood Pressure
Once the user enters the details and clicks "Predict Stroke Risk", the app will display the predicted stroke risk and confidence level.

### Example Output:
Stroke Risk Prediction: Yes
Confidence: 85.12%
