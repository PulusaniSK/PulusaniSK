Heart Disease Prediction:

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
heart_disease_data = pd.read_csv('heart_disease_data.csv')

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(heart_disease_data.drop('target', axis=1), heart_disease_data['target'], test_size=0.2, random_state=42)

# Train machine learning model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
