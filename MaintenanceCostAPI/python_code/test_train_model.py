import joblib
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def test_model_accuracy():
    test_df = pd.read_csv("testing_dataset.csv")  

    test_df['KmPerYear'] = test_df['KilometersDriven'] / test_df['AgeYears'].replace(0, 1)
    test_df['ServicesPerYear'] = test_df['NumServices'] / test_df['AgeYears'].replace(0, 1)
    test_df['IsNew'] = (test_df['AgeYears'] <= 3).astype(int)
    test_df['MaintenanceFrequency'] = test_df['NumServices'] / test_df['KilometersDriven'].replace(0, 1) * 10000

    X_test = test_df.drop("AnnualMaintenanceCostINR", axis=1)
    y_test = test_df["AnnualMaintenanceCostINR"]

    pipeline = joblib.load("model_pipeline.pkl")

    y_pred = pipeline.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)

    print(f"R² Score: {r2}")
    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"Mean Squared Error (MSE): {mse}")

    assert r2 > 0.7, f"Model R² score is too low: {r2}"
    assert mae < 10000, f"Model MAE is too high: {mae}"
    assert mse < 1e7, f"Model MSE is too high: {mse}"

    print("✅ All tests passed: Model accuracy and error metrics are acceptable.")

if __name__ == "__main__":
    test_model_accuracy()