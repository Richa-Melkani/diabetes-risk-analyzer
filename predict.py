import numpy as np
import joblib
import os

# Load model
base_path = os.path.dirname(__file__)
model_path = os.path.join(base_path, "model", "model.pkl")

model = joblib.load(model_path)

# 🔹 USER INPUT
print("Enter Patient Details:")

glucose = float(input("Glucose: "))
bp = float(input("Blood Pressure: "))
bmi = float(input("BMI: "))
age = float(input("Age: "))
dpf = float(input("Diabetes Pedigree Function: "))

# Create input array
input_data = np.array([[glucose, bp, bmi, age, dpf]])

prediction = model.predict(input_data)[0]

prob = model.predict_proba(input_data)[0][1]  # probability of diabetic

print("\nREPORT")

if prediction == 1:
    print("Status: Diabetic ")
else:
    print("Status: Not Diabetic ")

if prob < 0.30:
    risk = "Low Risk "
elif prob < 0.70:
    risk = "Medium Risk "
else:
    risk = "High Risk "

print(f"Risk Level: {risk}")
print(f"Probability: {prob*100:.2f}%")

print("\nSUGGESTIONS:")

if risk == "Low Risk ":
    print(" Maintain healthy diet")
    print(" Regular exercise (30 min daily)")
    print(" Routine health checkups")

elif risk == "Medium Risk ":
    print(" Reduce sugar intake")
    print(" Increase physical activity")
    print(" Monitor glucose regularly")
    print(" Consult doctor if needed")

else:  # High Risk
    print(" Consult a doctor immediately")
    print(" Follow strict diet plan")
    print(" Regular blood sugar monitoring")
    print(" Avoid junk food & sugary drinks")
