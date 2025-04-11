import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

df = pd.read_csv("maintenance_data.csv")
X = df.drop("AnnualMaintenanceCostINR", axis=1)
y = df["AnnualMaintenanceCostINR"]





categorical_cols = X.select_dtypes(include="object").columns.tolist()
preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)
], remainder="passthrough")

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(random_state=42))
])

pipeline.fit(X, y)

joblib.dump(pipeline, "model_pipeline.pkl")
