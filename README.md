# Diabetes Risk Analyzer 🩺

A Machine Learning based web application that predicts the risk of diabetes using health-related parameters.

The project is built using **Python, Flask, Random Forest Machine Learning Model, HTML, CSS, and JavaScript**.

---

# 🌐 Live Demo

🔗 Live Website:  
https://your-project-name.onrender.com

> Replace the above link with your actual Render deployment link after deployment.

---

# 🚀 Features

- Predicts diabetes risk using Machine Learning
- Uses Random Forest Classifier model
- Responsive and modern UI
- Displays:
  - Prediction Result
  - Risk Level
  - Probability Score
  - Health Suggestions
- Background image support
- Flask backend integration

---

# 🛠️ Technologies Used

## Frontend
- HTML5
- CSS3
- JavaScript

## Backend
- Python
- Flask

## Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Random Forest Classifier

---

# 📂 Project Structure

```bash
Diabetes-Risk-Analyzer/
│
├── app.py
├── model.py
├── predict.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── datasets/
│   └── diabetes.csv
│
├── model/
│   └── diabetes_model.pkl
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── img/
│       └── img_1.webp
│
├── templates/
│   └── index.html
│
└── screenshots/
    ├── img1.png
    ├── img2.png
    └── img3.png
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/Diabetes-Risk-Analyzer.git
```

---

## 2️⃣ Open Project Folder

```bash
cd Diabetes-Risk-Analyzer
```

---

## 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Train Machine Learning Model

```bash
python model.py
```

This generates the trained `.pkl` model file inside the `model/` folder.

---

## 5️⃣ Run Flask Application

```bash
python app.py
```

---

# 🌐 Open in Browser

```bash
http://127.0.0.1:5000
```

---

# 📊 Input Parameters

The application takes the following medical parameters:

- Glucose Level
- Blood Pressure
- BMI
- Age
- Diabetes Pedigree Function (DPF)

---

# 🧠 Machine Learning Model

- Algorithm Used: Random Forest Classifier
- Accuracy Achieved: **77.92%**
- Model File: `diabetes_model.pkl`

---

# 📸 Screenshots

## 🏠 Home Page

![Home Page](screenshots/img1.png)

---

## 📈 Prediction Result

![Prediction Result](screenshots/img2.png)

---

## ⚠️ Risk Analysis

![Risk Analysis](screenshots/img3.png)

---

# 🚀 Deployment

This project can be deployed on:

- Render
- Railway
- PythonAnywhere

Recommended Platform: **Render**

---

# 📌 Future Improvements

- Add more health parameters
- Improve prediction accuracy
- Add user authentication
- Store prediction history
- Add charts and analytics
- Mobile app integration

---

# 👩‍💻 Author

Developed by **Richa Melkani**

---

# 📜 License

This project is developed for educational and learning purposes only.