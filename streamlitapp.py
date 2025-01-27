import streamlit as st
import joblib
import pandas as pd

# Loading the pre-trained model
model = joblib.load('best_stroke_model.pkl')

def main():
    st.title("Stroke Risk Prediction App")

    st.write("### Input the details below:")

    # Creating dropdowns for categorical fields and inputs for numerical fields
    gender = st.selectbox("Gender", ["Male", "Female", "Other"], index=0)
    age = st.slider("Age", min_value=1, max_value=120, value=30)
    hypertension = st.selectbox("Hypertension", ["No", "Yes"], index=0)
    heart_disease = st.selectbox("Heart Disease", ["No", "Yes"], index=0)
    ever_married = st.selectbox("Ever Married", ["Yes", "No"], index=0)
    work_type = st.selectbox("Work Type", ["Private", "Self-employed", "children", "Never_worked", "Govt_job", "Salaried"], index=0)
    residence_type = st.selectbox("Residence Type", ["Urban", "Rural"], index=0)
    avg_glucose_level = st.number_input("Average Glucose Level", min_value=0.0, max_value=500.0, value=100.0, step=0.1)
    bmi = st.number_input("BMI", min_value=0.0, max_value=100.0, value=25.0, step=0.1)
    smoking_status = st.selectbox("Smoking Status", ["formerly smoked", "never smoked", "smokes", "Not specified"], index=0)
    high_blood_pressure = st.selectbox("High Blood Pressure", ["No", "Yes"], index=0)

    # Converting categorical values to numeric for model compatibility
    categorical_mapping = {
        "Yes": 1,
        "No": 0,
        "Male": 1,
        "Female": 2,
        "Other": 3,
    }

    # Preparing input data
    input_data = {
        "gender": categorical_mapping.get(gender, gender),
        "age": age,
        "hypertension": categorical_mapping.get(hypertension, hypertension),
        "heart_disease": categorical_mapping.get(heart_disease, heart_disease),
        "ever_married": categorical_mapping.get(ever_married, ever_married),
        "work_type": work_type,
        "Residence_type": residence_type,
        "avg_glucose_level": avg_glucose_level,
        "bmi": bmi,
        "smoking_status": smoking_status,
        "high_blood_pressure": categorical_mapping.get(high_blood_pressure, high_blood_pressure),
    }

    # Display prediction when the button is clicked
    if st.button("Predict Stroke Risk"):
        try:
            input_df = pd.DataFrame([input_data])
            prediction = model.predict(input_df)[0]
            confidence = model.predict_proba(input_df)[0][1]

            st.write(f"### Stroke Risk Prediction: {'Yes' if prediction == 1 else 'No'}")
            st.write(f"#### Confidence: {confidence * 100:.2f}%")
        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
