# 🩺 Diabetes Risk Analyzer

A Machine Learning-based web application that predicts the risk of diabetes using health parameters such as glucose level, blood pressure, BMI, age, and diabetes pedigree function. The model is trained using Random Forest and deployed using Flask on Render.

---

## 🚀 Features

- Predict diabetes risk instantly
- Shows result: Diabetic / Not Diabetic
- Displays risk level: Low / Medium / High
- Shows probability percentage
- Gives health suggestions
- Clean glassmorphism UI design
- Fully responsive web interface

---

## 🧠 Machine Learning Model

- Algorithm: Random Forest Classifier
- Library: Scikit-learn
- Handles missing values (0 replaced with median)
- Outputs probability-based prediction
- Trained on standard diabetes dataset

---
## 📈 Model Performance

- Current Accuracy: 77.92%
- Dataset preprocessing improves prediction quality
- Trained using train-test split method
- Random Forest helps reduce overfitting

---
## 📊 Input Features and their Ranges

| Feature        | Low    | Medium        | High    |
| -------------- | ------ | ------------- | ------- |
| Glucose        | <70    | 100–125       | ≥126    |
| Blood Pressure | <90/60 | 120/80–139/89 | ≥140/90 |
| BMI            | <18.5  | 25–29.9       | ≥30     |
| Age            | <30    | 30–50         | >50     |
| DPF            | 0–0.4  | 0.4–1.0       | >1.0    |

---

## 📂 Project Structure
```
Diabetes-Risk-Analyzer/

├── app.py
├── model.py
├── predict.py
├── requirements.txt
├── Procfile

├── model/
│   └── model.pkl

├── dataset/
│   └── diabetes.csv

├── static/
│   ├── style.css
│   ├── script.js
│   └── img/bg_9.webp

├── templates/
│   └── index.html

└── snapshots/
    ├── home-page_ui.png
    └── prediction_result.png
```
---
## ⚙️ Installation & Setup

### 1. Clone Repository
```
git clone https://github.com/your-username/diabetes-risk-analyzer.git
cd diabetes-risk-analyzer
```
---

### 2. Install Dependencies
```
pip install -r requirements.txt
```
---

### 3. Train Model (First Time Only)
```
python model.py
```
---

### 4. Run Flask App
```
python app.py
```
Open in browser:
```
http://127.0.0.1:5000/
```
---

## ☁️ Deployment

- Platform: Render
- Backend: Flask
- Server: Gunicorn
- Model: joblib saved Random Forest model

---

## 🛠️ Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML, CSS, JavaScript
- Render

---

## 🚀 Live Demo

👉 https://diabetes-risk-analyzer-vkj3.onrender.com/

---

## 📸 Snapshots

### Home Page
![Home Page](snapshots/home-page_ui.png)

### Prediction Result
![Prediction Result](snapshots/prediction_result.png)

---
## 📈 Future Improvements

- Add more medical features
- Improve accuracy using XGBoost
- Add login system
- Store prediction history
- Mobile app version

---

## ⚠️ Disclaimer

This project is developed for educational purposes only and should not be considered a substitute for professional medical diagnosis.
---

## 👩‍💻 Author

Richa Melkani

---

## 📜 License

MIT License
