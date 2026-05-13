import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#  File path
base_path = os.path.dirname(__file__)
data_path = os.path.join(base_path, "dataset", "diabetes.csv")

df = pd.read_csv(data_path)

# Fix invalid 0 values
cols_with_zero = ['Glucose', 'BloodPressure', 'BMI']

for col in cols_with_zero:
    df[col] = df[col].replace(0, df[col].median())


# df = df.drop(columns=['DiabetesPedigreeFunction'], errors='ignore')

#  Features & target
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


model = RandomForestClassifier(
    n_estimators=350,
    max_depth=7,
    min_samples_split=4,
    min_samples_leaf=2,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy in %
accuracy = accuracy_score(y_test, y_pred) * 100
print(f"Model Accuracy: {accuracy:.2f}%")

# Create model folder
model_folder = os.path.join(base_path, "model")
os.makedirs(model_folder, exist_ok=True)

# Save model
model_path = os.path.join(model_folder, "model.pkl")
joblib.dump(model, model_path)

print("model trained successfully")