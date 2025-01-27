from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('best_stroke_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        required_fields = ['gender', 'age', 'hypertension', 'heart_disease',
                          'ever_married', 'work_type', 'Residence_type',
                          'avg_glucose_level', 'bmi', 'smoking_status',
                          'high_blood_pressure']
        
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
            
        input_df = pd.DataFrame([data])
        prediction = model.predict(input_df)[0]
        return jsonify({
            'stroke_risk': int(prediction), 
            'confidence': float(model.predict_proba(input_df)[0][1])
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)