import pandas as pd
import numpy as np
from scipy import stats
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
import joblib


df = pd.read_csv("maintenance_data.csv")


df['KmPerYear'] = df['KilometersDriven'] / df['AgeYears']
df['ServicesPerYear'] = df['NumServices'] / df['AgeYears']
df['IsNew'] = (df['AgeYears'] <= 3).astype(int)
df['MaintenanceFrequency'] = df['NumServices'] / df['KilometersDriven'] * 10000


def remove_outliers(df, columns, z_threshold=3):
    df_clean = df.copy()
    for col in columns:
        z_scores = stats.zscore(df_clean[col])
        df_clean = df_clean[abs(z_scores) < z_threshold]
    return df_clean

numerical_cols = ['AgeYears', 'KilometersDriven', 'NumServices', 'KmPerYear', 
                 'ServicesPerYear', 'MaintenanceFrequency']
df_cleaned = remove_outliers(df, numerical_cols)


X = df_cleaned.drop("AnnualMaintenanceCostINR", axis=1)
y = df_cleaned["AnnualMaintenanceCostINR"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


categorical_cols = X.select_dtypes(include="object").columns.tolist()
numeric_cols = X.select_dtypes(exclude="object").columns.tolist()

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numeric_cols),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)
])

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(random_state=42))
])

param_grid = {
    'regressor__n_estimators': [100, 200, 300],
    'regressor__max_depth': [None, 10, 20],
    'regressor__min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(
    pipeline, param_grid, cv=5, 
    scoring='neg_mean_squared_error', 
    n_jobs=-1
)
grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_

y_pred = best_model.predict(X_test)
print(f"Best Parameters: {grid_search.best_params_}")
print(f"R2 Score: {r2_score(y_test, y_pred):.3f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.2f}")


cv_scores = cross_val_score(best_model, X, y, cv=5, 
                           scoring='neg_mean_squared_error')
rmse_scores = np.sqrt(-cv_scores)
print(f"Cross-validation RMSE scores: {rmse_scores}")
print(f"Average RMSE: {rmse_scores.mean():.2f} (+/- {rmse_scores.std() * 2:.2f})")


feature_names = (numeric_cols + categorical_cols)
importances = best_model.named_steps['regressor'].feature_importances_
for name, importance in sorted(zip(feature_names, importances), 
                             key=lambda x: x[1], reverse=True):
    print(f"{name}: {importance:.3f}")

joblib.dump(best_model, "model_pipeline.pkl")