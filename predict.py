# This is a sample script to check whether the model works

import pickle
import pandas as pd

# Load the saved model
with open("models/final_random_forest_model.pkl", "rb") as file:
    model = pickle.load(file)

# Example input: Replace this with real input for actual use
sample_passenger = {
    'Pclass': 3,
    'Sex': 0,          # male
    'Embarked': 2,      # C
    'FamilySize': 1,
    'IsAlone': 1,
    'Title': 1,         # Mr
    'AgeGroup': 2,
    'FareBand': 1
}

# Convert to DataFrame
sample_df = pd.DataFrame([sample_passenger])

# Predict
prediction = model.predict(sample_df)
print("Prediction:", "Survived" if prediction[0] == 1 else "Did Not Survive")
