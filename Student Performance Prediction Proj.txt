Student Performance Prediction: Project 

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

# Load dataset
student_data = pd.read_csv('student_data.csv')

# Handle missing values
imputer = SimpleImputer(strategy='mean')
student_data['missing_col'] = imputer.fit_transform(student_data[['missing_col']])

# Encode categorical variables
encoder = OneHotEncoder()
encoded_data = encoder.fit_transform(student_data[['categorical_col']])

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(encoded_data, student_data['target'], test_size=0.2, random_state=42)

# Train machine learning model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
