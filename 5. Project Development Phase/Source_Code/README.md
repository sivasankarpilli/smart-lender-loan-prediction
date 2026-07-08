# Smart Lender –Loan Approval Prediction System

# Overview

**Smart Lender** is an Artificial Intelligence and Machine Learning based web application that predicts whether a customer's loan application should be approved or rejected based on their personal and financial information.

Banks and financial institutions receive thousands of loan applications every day. Evaluating each application manually consumes significant time and resources while increasing the possibility of human errors. This project automates the loan approval process by using a trained Machine Learning model to analyze applicant details and provide an instant prediction.

The application has been developed using **Python, Flask, HTML, CSS, and XGBoost**, offering a simple web interface for users while performing intelligent predictions in the backend.

---

# Technologies Used

## Programming Language

- Python

## Frontend

- HTML5
- CSS3

## Backend

- Flask

## Machine Learning Libraries

- Scikit-learn
- XGBoost
- NumPy
- Pandas
- Pickle

## Development Tools

- Jupyter Notebook
- VS Code

---

# Machine Learning Model

The project uses the **XGBoost Classifier**, a powerful ensemble learning algorithm based on gradient boosting.

### Why XGBoost?

- High prediction accuracy
- Fast training
- Handles missing values efficiently
- Prevents overfitting
- Suitable for structured datasets
- Widely used in banking and finance

---

# Project Structure

```
Smart_Lender_Project_Code/
│
├── Dataset/
│   └── loan_prediction.csv
│
├── Flask/
│   │
│   ├── app.py
│   ├── requirements.txt
│   ├── xgb_model.pkl
│   ├── scale1.pkl
│   │
│   ├── Templates/
│   │     ├── index.html
│   │     └── result.html
│   │
│   └── Static/
│         ├── style.css
│         └── background.jpeg
│
├── Training/
│   └── Smart Lender Using ML.ipynb
│
├── Project_Screenshot_Images.pdf
│
└── README.md
```

---

# Dataset Description

The dataset contains historical loan application records collected from previous applicants.

Each record consists of demographic, financial, and credit-related information.

### Dataset Features

| Feature | Description |
|----------|-------------|
| Gender | Male/Female |
| Married | Marital Status |
| Dependents | Number of Dependents |
| Education | Graduate/Not Graduate |
| Self Employed | Employment Status |
| Applicant Income | Monthly Income |
| Coapplicant Income | Co-applicant Monthly Income |
| Loan Amount | Requested Loan Amount |
| Loan Amount Term | Loan Duration |
| Credit History | Credit Score History |
| Property Area | Urban/Semiurban/Rural |
| Loan Status | Approved/Rejected |

---

# Working of the Project

The project follows the complete Machine Learning pipeline.

## Step 1

Collect historical loan application data.

↓

## Step 2

Clean the dataset by handling missing values.

↓

## Step 3

Encode categorical variables into numerical values.

↓

## Step 4

Scale numerical features using StandardScaler.

↓

## Step 5

Train the XGBoost model.

↓

## Step 6

Evaluate model accuracy.

↓

## Step 7

Save the trained model using Pickle.

↓

## Step 8

Deploy the model using Flask.

↓

## Step 9

Accept user inputs from the web page.

↓

## Step 10

Predict loan approval status.

---

# Data Preprocessing

Before training, the following preprocessing steps are performed:

- Missing value handling
- Label Encoding
- Feature Scaling
- Data Cleaning
- Feature Selection
- Train-Test Split

---

# Prediction Workflow

```
User Inputs

        ↓

HTML Form

        ↓

Flask Backend

        ↓

Data Preprocessing

        ↓

Feature Scaling

        ↓

XGBoost Model

        ↓

Prediction

        ↓

Loan Approved / Loan Rejected
```

---

# Input Parameters

The application requires the following inputs:

- Gender
- Married
- Dependents
- Education
- Self Employed
- Applicant Income
- Co-applicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

---

# Output

The trained model predicts one of the following outcomes:

### Loan Approved

The applicant satisfies the conditions for loan approval.

or

### Loan Rejected

The applicant does not satisfy the loan eligibility criteria.

---

# Installation Guide

## Step 1

Clone the repository

```bash
git clone https://github.com/yourusername/Smart-Lender.git
```

---

## Step 2

Navigate to project folder

```bash
cd Smart-Lender/Flask
```

---

## Step 3

Create virtual environment

```bash
python -m venv venv
```

---

## Step 4

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Step 5

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Step 6

Run Flask server

```bash
python app.py
```

---

## Step 7

Open Browser

```
http://127.0.0.1:5000
```

---

# 📸 Screenshots

Include screenshots of:

- Home/Loan Application Form
- Prediction Result
- Approved Loan Page
- Rejected Loan Page

---

# 📊 Future Scope

This project can be enhanced by adding:

- User Authentication
- Database Integration
- Admin Dashboard
- Loan History Tracking
- EMI Calculator
- Credit Score API
- Explainable AI (SHAP/LIME)
- Multiple ML Model Comparison
- Cloud Deployment (AWS/Azure/GCP)
- Mobile Application
- REST API Support

---


# 📚 Requirements

Software Requirements

- Python 3.10+
- Flask
- Jupyter Notebook
- VS Code

Python Libraries

```text
Flask
NumPy
Pandas
Scikit-learn
XGBoost
Pickle
```

Install all libraries

```bash
pip install -r requirements.txt
```

---

# Team Members

| Name | Role |
|------|------|
| Jeeru Mitravardhan | Team Lead |
| Chekuri Devi | Team Member |
| Ganthala Rohith | Team Member |
| Pilli Siva Sankar | Team Member |
| Yelugubanti Satya Bhavani | Team Member |

---

# Internship Information

**Project Title:** Smart Lender – Loan Approval Prediction

**Domain:** Artificial Intelligence & Machine Learning

**Technology Stack:** Python, Flask, HTML, CSS, XGBoost

**Project Type:** Machine Learning Web Application

**Purpose:** SmartBridge Internship Project

---

# Acknowledgements

We sincerely thank our faculty mentors, project guides, and everyone who contributed to the successful completion of this project.
