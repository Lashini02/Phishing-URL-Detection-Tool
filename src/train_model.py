import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from feature_extractor import extract_features


def main():
    data_path = os.path.join("data", "urls.csv")
    model_folder = "model"
    model_path = os.path.join(model_folder, "phishing_model.pkl")

    # Check whether dataset exists
    if not os.path.exists(data_path):
        print("Dataset not found:", data_path)
        return

    # Read dataset
    df = pd.read_csv(data_path)

    # Check required columns
    if "url" not in df.columns or "label" not in df.columns:
        print("CSV file must contain 'url' and 'label' columns.")
        return

    # Extract features from each URL
    feature_list = df["url"].apply(extract_features)
    X = pd.DataFrame(feature_list.tolist())
    y = df["label"]

    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Create model
    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    # Train model
    model.fit(X_train, y_train)

    # Predict on test data
    y_pred = model.predict(X_test)

    # Show results
    print("\n=== MODEL EVALUATION ===")
    print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # Save model
    os.makedirs(model_folder, exist_ok=True)
    joblib.dump(model, model_path)

    print(f"\nModel saved successfully to: {model_path}")
    print("\nFeatures used:")
    print(list(X.columns))


if __name__ == "__main__":
    main()