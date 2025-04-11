from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("model_pipeline.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    input_df = pd.DataFrame([data])
    prediction = model.predict(input_df)
    return jsonify({"PredictedAnnualMaintenanceCostINR": prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)
