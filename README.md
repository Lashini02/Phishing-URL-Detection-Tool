# Phishing URL Detection Tool

# Project Overview

Phishing attacks are one of the most common cybersecurity threats today. Attackers often create fake websites that look similar to legitimate ones in order to steal user credentials, financial data, or other sensitive information.

This project is a Machine Learning based Phishing URL Detection Tool developed using Python. The goal of the project is to analyze the structure of a website URL and predict whether it is likely to be a phishing website or a legitimate website.

Instead of relying on external APIs or blacklists, this tool focuses on URL feature analysis. It extracts several characteristics from a given URL and uses a trained machine learning model to determine whether the URL shows suspicious patterns.

This project was built as a cybersecurity and machine learning practice project and is suitable for demonstrating practical skills in Python, data processing, and basic security analysis.

## Why This Project?

Phishing websites often contain suspicious patterns such as:

unusually long URLs
multiple subdomains
suspicious keywords like login, verify, secure
use of IP addresses instead of domain names
excessive symbols or special characters

By analyzing these patterns, we can train a machine learning model to recognize potentially malicious URLs.

The purpose of this project is to demonstrate how machine learning can assist in detecting phishing attempts using URL analysis.

## Features

This tool provides the following features:

- Extracts structural features from URLs
- Detects suspicious keywords within URLs
- Identifies potential phishing indicators
- Uses a machine learning classifier for prediction
- Displays detailed feature analysis for each URL
- Outputs phishing probability and classification result

## Technologies Used

- Python
- pandas
- scikit-learn
- joblib

## Project Structure

```bash
phishing-url-detector/
│
├── data/
│   └── urls.csv
├── model/
├── src/
│   ├── feature_extractor.py
│   ├── train_model.py
│   └── predict.py
├── requirements.txt
├── README.md
└── .gitignore

```

## How the System Works

The system works in three main stages.

1. URL Feature Extraction

The system analyzes the input URL and extracts several features such as:

URL length
number of dots
number of hyphens
number of digits
use of HTTPS
presence of suspicious keywords
number of subdomains
use of IP address in the URL

These features help the model identify patterns that are commonly associated with phishing websites.

2. Model Training

The dataset (urls.csv) contains labeled URLs:

0 = legitimate website
1 = phishing website

The system converts each URL into numerical features and trains a Random Forest classifier using these features.

The trained model is saved as:

```model/phishing_model.pkl```

3. URL Prediction

When a user enters a URL, the program:

extracts the same set of features
loads the trained model
predicts whether the URL is phishing or legitimate
displays prediction probability

Example output:

```
=== PREDICTION RESULT ===
Result: PHISHING URL
Phishing Probability: 100.00%
Legitimate Probability: 0.00%
```
## Installation Guide
Step 1 — Clone the Repository
```
git clone https://github.com/yourusername/phishing-url-detector.git
cd phishing-url-detector
```
Step 2 — Install Required Libraries
```
pip install -r requirements.txt
```
Step 3 — Train the Model

Run the training script:
```
python src/train_model.py
```
This will:

read the dataset
extract features
train the machine learning model
save the trained model

Step 4 — Predict URLs

After training, run:
```
python src/predict.py
```
Example:
```
Enter a URL to analyze:
http://secure-bank-login-update.xyz
```
Output example:
```
Result: PHISHING URL
Phishing Probability: 91.25%
```

## Example URLs to Test

Legitimate examples:
```
https://google.com
https://github.com
https://openai.com
```
Phishing-style examples:
```
http://secure-bank-login-update.xyz
http://verify-paypal-login-security.com
http://free-gift-card-win-now.ru

```

## Dataset
The dataset used in this project contains URLs labeled as either legitimate or phishing.

Example dataset format:
```
url,label
http://google.com,0
https://github.com,0
http://verify-paypal-login-security.com,1
```

For demonstration purposes, a small dataset is included in the repository.
For better accuracy, the model should be trained on larger phishing datasets.

## Limitations

This project is a prototype system and has several limitations:

- small dataset size
- only URL-based features are used
- no domain reputation analysis
- no DNS or WHOIS features
- no webpage content analysis

Therefore, it should not be considered a full phishing detection system.

## Future Improvements
This project can be improved in several ways:

- using a larger phishing dataset
- adding domain age analysis (WHOIS)
- detecting shortened URLs
- analyzing webpage content
- implementing deep learning models
- building a web interface using Flask or Streamlit
- creating a browser extension for phishing detection

## Learning Outcomes
This project helped practice the following concepts:

- Python programming
- data preprocessing
- feature engineering
- machine learning classification
- cybersecurity threat analysis
- GitHub project management


## Author
D.V. Lashini Chamodi

