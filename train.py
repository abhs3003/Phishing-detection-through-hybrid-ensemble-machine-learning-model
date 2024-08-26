import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import joblib

# Load dataset
data = pd.read_csv('dataset/phishing.csv')
# Extract labels and features
y = data['Classification'].values  # Assuming 'class' is the name of the target variable column
X = data.drop('Classification', axis=1).values



# Initialize base classifiers
logistic_regression = LogisticRegression(C=1, max_iter=1000)
support_vector_machine = SVC(C=1, kernel='rbf', probability=True)
decision_tree = DecisionTreeClassifier(max_depth=None)

# Initializing the ensemble model
ensemble_model = VotingClassifier(estimators=[
    ('logistic_regression', logistic_regression),
    ('support_vector_machine', support_vector_machine),
    ('decision_tree', decision_tree)
], voting='soft')

# Train the ensemble model on the entire training set
ensemble_model.fit(X, y)

# Save the trained model
joblib.dump(ensemble_model, 'classifier/ensemble_model.pkl', compress=9)