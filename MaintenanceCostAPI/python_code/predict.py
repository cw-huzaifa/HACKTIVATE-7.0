import sys
import json
import joblib
import pandas as pd
import numpy as np

model = joblib.load("model_pipeline.pkl")

def preprocess_input(data):
    # Convert dict to DataFrame
    df = pd.DataFrame([data])

    # Derived columns (same as training script)
    df['KmPerYear'] = df['KilometersDriven'] / df['AgeYears']
    df['ServicesPerYear'] = df['NumServices'] / df['AgeYears']
    df['IsNew'] = (df['AgeYears'] <= 3).astype(int)
    df['MaintenanceFrequency'] = df['NumServices'] / df['KilometersDriven'] * 10000

    return df

def main():
    if len(sys.argv) < 2:
        print("No input data provided.")
        return

    # Read input JSON from command-line argument
    input_json = sys.argv[1]
    input_data = json.loads(input_json)

    # Preprocess the input data
    df = preprocess_input(input_data)

    # Predict maintenance cost
    prediction = model.predict(df)[0]

    # Print result so .NET can capture it
    print(round(prediction, 2))

if __name__ == "__main__":
    main()