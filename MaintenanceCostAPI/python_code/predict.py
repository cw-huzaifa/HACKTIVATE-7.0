import os
import sys
import json
import joblib
import pandas as pd
import numpy as np

script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, "model_pipeline.pkl")

model = joblib.load(model_path)

def safe_divide(a, b):
    return a / b if b != 0 else 0

def preprocess_input(data):
    # Convert dict to DataFrame
    df = pd.DataFrame([data])

    df = df.rename(columns={
        "brand": "Brand",
        "model": "Model",
        "fuelType": "FuelType",
        "transmission": "Transmission",
        "ageYears": "AgeYears",
        "kilometersDriven": "KilometersDriven",
        "numServices": "NumServices",
        "drivingBehavior": "DrivingBehavior"
    })

    df['KmPerYear'] = df.apply(lambda row: safe_divide(row['KilometersDriven'], row['AgeYears']), axis=1)
    df['ServicesPerYear'] = df.apply(lambda row: safe_divide(row['NumServices'], row['AgeYears']), axis=1)
    df['IsNew'] = (df['AgeYears'] <= 3).astype(int)
    df['MaintenanceFrequency'] = df.apply(lambda row: safe_divide(row['NumServices'], row['KilometersDriven']) * 10000, axis=1)

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