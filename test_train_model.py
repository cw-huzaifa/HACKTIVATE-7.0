# import joblib
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import r2_score
# from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# # filepath: c:\Users\huzaifa.qureshi\Documents\carwale\HACKTIVATE-7.0\test_train_model.py

# def test_model_accuracy():
#     # Load the dataset
#     df = pd.read_csv("test_train_model.csv")
#     X = df.drop("AnnualMaintenanceCostINR", axis=1)
#     y = df["AnnualMaintenanceCostINR"]

#     # Split the data into training and testing sets
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#     def test_model_accuracy():
#         # Load the dataset
#         df = pd.read_csv("test_train_model.csv")
#         X = df.drop("AnnualMaintenanceCostINR", axis=1)
#         y = df["AnnualMaintenanceCostINR"]

#         # Split the data into training and testing sets
#         X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#         # Load the saved model pipeline
#         pipeline = joblib.load("model_pipeline.pkl")

#         # Make predictions on the test set
#         y_pred = pipeline.predict(X_test)

#         # Calculate the R² score
#         r2 = r2_score(y_test, y_pred)
#         assert r2 > 0.7, f"Model R² score is too low: {r2}"

#         # Calculate Mean Absolute Error (MAE)
#         mae = mean_absolute_error(y_test, y_pred)
#         print(f"Mean Absolute Error (MAE): {mae}")

#         # Calculate Mean Squared Error (MSE)
#         mse = mean_squared_error(y_test, y_pred)
#         print(f"Mean Squared Error (MSE): {mse}")

#         # Assert that MAE and MSE are within acceptable ranges
#         assert mae < 10000, f"Model MAE is too high: {mae}"
#         assert mse < 1e7, f"Model MSE is too high: {mse}"

#     if __name__ == "__main__":
#         test_model_accuracy()
#         print("All tests passed: Model accuracy and error metrics are acceptable.")

import joblib
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def test_model_accuracy():
    # Load the test dataset
    test_df = pd.read_csv("testing_dataset.csv")  # This is your separate test dataset
    X_test = test_df.drop("AnnualMaintenanceCostINR", axis=1)
    y_test = test_df["AnnualMaintenanceCostINR"]

    print("Test columns:")
    print(X_test.columns)
    print(X_test.dtypes)

    # Load the saved model pipeline (already trained on different data)
    pipeline = joblib.load("model_pipeline.pkl")

    # Make predictions
    y_pred = pipeline.predict(X_test)

    # Calculate and print metrics
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)

    print(f"R² Score: {r2}")
    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"Mean Squared Error (MSE): {mse}")

    # Optional assertions
    assert r2 > 0.7, f"Model R² score is too low: {r2}"
    assert mae < 10000, f"Model MAE is too high: {mae}"
    assert mse < 1e7, f"Model MSE is too high: {mse}"

    print("✅ All tests passed: Model accuracy and error metrics are acceptable.")

if __name__ == "__main__":
    test_model_accuracy()
