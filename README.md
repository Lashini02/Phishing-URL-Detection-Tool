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


 How the System Works
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

\*\*model/phishing_model.pkl

3. URL Prediction

When a user enters a URL, the program:

extracts the same set of features
loads the trained model
predicts whether the URL is phishing or legitimate
displays prediction probability

Example output:

=== PREDICTION RESULT ===
Result: PHISHING URL
Phishing Probability: 100.00%
Legitimate Probability: 0.00%

```
##
```
