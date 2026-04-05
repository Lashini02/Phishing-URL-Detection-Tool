import os
import joblib
import pandas as pd

from feature_extractor import extract_features


def main():
    model_path = os.path.join("model", "phishing_model.pkl")

    if not os.path.exists(model_path):
        print("Model file not found.")
        print("Please run train_model.py first.")
        return

    model = joblib.load(model_path)

    url = input("Enter a URL to analyze: ").strip()

    if not url:
        print("No URL entered.")
        return

    features = extract_features(url)
    X_input = pd.DataFrame([features])

    prediction = model.predict(X_input)[0]

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(X_input)[0]
        phishing_probability = probabilities[1] * 100
        legitimate_probability = probabilities[0] * 100
    else:
        phishing_probability = None
        legitimate_probability = None

    print("\n=== EXTRACTED FEATURES ===")
    for key, value in features.items():
        print(f"{key}: {value}")

    print("\n=== PREDICTION RESULT ===")
    if prediction == 1:
        print("Result: PHISHING URL")
    else:
        print("Result: LEGITIMATE URL")

    if phishing_probability is not None:
        print(f"Phishing Probability: {phishing_probability:.2f}%")
        print(f"Legitimate Probability: {legitimate_probability:.2f}%")


if __name__ == "__main__":
    main()