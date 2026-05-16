from flask import Flask, render_template, request
import numpy as np
import joblib
import os

app = Flask(__name__)

# Load model
base_path = os.path.dirname(__file__)
model_path = os.path.join(base_path, "model", "model.pkl")
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        glucose = float(request.form['Glucose'])
        bp = float(request.form['BloodPressure'])
        bmi = float(request.form['BMI'])
        age = float(request.form['Age'])
        dpf = float(request.form['DPF'])

        input_data = np.array([[glucose, bp, bmi, dpf, age]])

        prediction = model.predict(input_data)[0]
        prob = model.predict_proba(input_data)[0][1]

        # FINAL LOGIC
        if prediction == 1:
            status = "Diabetic"

            if prob < 0.30:
                risk = "Low Risk"
                suggestion = "Maintain a balanced diet and regular exercise."
            elif prob < 0.70:
                risk = "Medium Risk"
                suggestion = "Control sugar intake, stay active, and monitor glucose levels."
            else:
                risk = "High Risk"
                suggestion = "Consult a doctor immediately and follow a strict health plan."

        else:
            status = "Not Diabetic"
            risk = ""
            suggestion = "You are healthy. Maintain a good lifestyle."

        return render_template(
            'index.html',
            prediction_text=status,
            risk_text=risk,
            prob_text=f"{prob*100:.2f}%",
            suggestion_text=suggestion
        )

    except:
        return render_template(
            'index.html',
            prediction_text="Error in input ❌"
        )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)