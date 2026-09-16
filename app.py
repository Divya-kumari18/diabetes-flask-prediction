from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load trained model and scaler
model = joblib.load("diabetes_model.pkl")
scaler = joblib.load("diabetes_scaler.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get values from HTML form
        pregnancies = float(request.form["pregnancies"])
        glucose = float(request.form["glucose"])
        blood_pressure = float(request.form["blood_pressure"])
        skin_thickness = float(request.form["skin_thickness"])
        insulin = float(request.form["insulin"])
        bmi = float(request.form["bmi"])
        diabetes_pedigree = float(request.form["diabetes_pedigree"])
        age = float(request.form["age"])

        # Create input array
        input_data = np.array([[
            pregnancies,
            glucose,
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            diabetes_pedigree,
            age
        ]])

        # Scale input
        input_scaled = scaler.transform(input_data)

        # Prediction
        prediction = model.predict(input_scaled)[0]

        # Probability
        probability = model.predict_proba(input_scaled)[0][1]

        if prediction == 1:
            result = "Higher predicted likelihood of diabetes"
        else:
            result = "Lower predicted likelihood of diabetes"

        return render_template(
            "index.html",
            prediction=result,
            probability=round(probability * 100, 2)
        )

    except Exception as e:
        return render_template(
            "index.html",
            error="Please enter valid values."
        )


# API endpoint
@app.route("/api/predict", methods=["POST"])
def api_predict():

    try:
        data = request.get_json()

        input_data = np.array([[
            data["Pregnancies"],
            data["Glucose"],
            data["BloodPressure"],
            data["SkinThickness"],
            data["Insulin"],
            data["BMI"],
            data["DiabetesPedigreeFunction"],
            data["Age"]
        ]])

        # Scale input
        input_scaled = scaler.transform(input_data)

        # Prediction
        prediction = int(model.predict(input_scaled)[0])

        # Probability
        probability = float(
            model.predict_proba(input_scaled)[0][1]
        )

        return jsonify({
            "prediction": prediction,
            "probability": round(probability * 100, 2)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
