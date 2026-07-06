# smart-lender-loan-prediction
AI-powered Smart Lender project developed as part of the SmartBridge internship.

🏦 Smart Lender - Loan Approval & Applicant Eligibility Prediction System
![Python](https://www.python.org/)
![Flask](https://flask.palletsprojects.com/)
![Machine Learning](https://xgboost.readthedocs.io/)
![License](LICENSE)
Smart Lender is an end-to-end Machine Learning web solution designed to automate loan application risk assessment and applicant eligibility evaluation. By assessing key financial, credit, demographic, and background parameters, Smart Lender provides instant, data-driven loan approval decisions (`Loan Approved ✅` or `Loan Rejected ❌`), helping financial institutions reduce manual evaluation time, lower risk, and maintain consistent lending practices.
---
📌 Table of Contents
Overview
Key Features
System Architecture
Project Directory Structure
Machine Learning Pipeline
Input Features & Schema
Installation & Setup
Usage Guide
Project SDLC Phases
Future Enhancements
License & Acknowledgments
---
💡 Overview
Loan evaluation processes in modern banking often suffer from manual processing delays, inconsistent decision logic, and susceptibility to human error. Smart Lender leverages Machine Learning algorithms (such as XGBoost and Random Forest Classifiers) trained on historical loan data to instantly predict loan eligibility based on applicant profiles.
The project encompasses the complete Software Development Life Cycle (SDLC), from initial brainstorming and requirement analysis to model training, Flask web deployment, testing, and project demonstration.
---
✨ Key Features
Instant Automated Decisioning: Evaluates customer loan applications in real time.
Machine Learning Powered: Uses pre-trained XGBoost model (`xgb\\\_model.pkl`) coupled with feature scaling (`scale1.pkl`).
User-Friendly Web Interface: Intuitive HTML/CSS frontend served via Flask.
Data Preprocessing & Scaling: Handles numerical transform, categorical mapping, and missing value imputations.
Comprehensive Project Documentation: Structured documentation covering all 8 SDLC project lifecycle phases.
---
🏗️ System Architecture
```
+------------------+       +-------------------+       +-----------------------+
|  Web Interface   | ----> |   Flask Server    | ----> |  StandardScaler       |
| (Applicant Data) | POST  |   (`app.py`)      | Transform|  (`scale1.pkl`)       |
+------------------+       +-------------------+       +-----------------------+
                                                                   |
                                                                   v
+------------------+       +-------------------+       +-----------------------+
|  Result Page     | <---- | Prediction Output | <---- | XGBoost ML Model      |
| (`result.html`)  |       | (Approved/Denied) |       | (`xgb\\\_model.pkl`)     |
+------------------+       +-------------------+       +-----------------------+
```
---
📁 Project Directory Structure
```
Smart\\\_Lender\\\_Documentation/
│
├── 1. Brainstorming \\\& Ideation/
│   ├── Brainstorming \\\& Idea Prioritization.pdf
│   ├── Define Problem Statements.pdf
│   └── Empathy Map.pdf
│
├── 2. Requirement Analysis/
│   ├── Customer Journey Map.pdf
│   ├── Data Flow Diagram.pdf
│   ├── Solution Requirements.pdf
│   └── Technology Stack.pdf
│
├── 3. Project Design Phase/
│   ├── Problem-Solution Fit.pdf
│   ├── Proposed Solution.pdf
│   └── Solution Architecture.pdf
│
├── 4. Project Planning Phase/
│   └── Project Planning.pdf
│
├── 5. Project Development Phase/
│   ├── Code-Layout, Readability and Reusability.pdf
│   ├── Coding \\\& Solution.pdf
│   ├── No. of Functional Features Included in the Solution.pdf
│   └── Smart\\\_Lender\\\_Code/
│       ├── Dataset/
│       │   └── loan\\\_prediction.xlsx - loan\\\_prediction.csv
│       └── Flask/
│           ├── app.py
│           ├── scale1.pkl
│           ├── xgb\\\_model.pkl
│           ├── requirements.txt
│           ├── Static/
│           ├── Templates/
│           │   ├── index.html
│           │   └── result.html
│           └── Training/
│               └── Smart Lender Using ML.ipynb
│
├── 6.Project Testing/
│   └── Performance Testing.pdf
│
├── 7.Project Documentation/
│   ├── Project Executable Files.pdf
│   └── Sample Project Documentation.pdf
│
└── 8.Project Demonstration/
    ├── Communication.pdf
    ├── Demonstration of Proposed Features.pdf
    ├── Project Demo Planning.pdf
    ├── Scalability \\\& Future Plan.pdf
    └── Team Involvement in Demonstration.pdf
```
---
📊 Input Features & Schema
The model accepts 11 input features collected via the web application form:
Feature Name	Description	Values / Encoding
Gender	Applicant's Gender	`1` (Male), `0` (Female)
Married	Marital Status	`1` (Yes), `0` (No)
Dependents	Number of Dependents	`0`, `1`, `2`, `3+` (encoded)
Education	Educational Qualification	`1` (Graduate), `0` (Not Graduate)
Self_Employed	Employment Status	`1` (Yes), `0` (No)
ApplicantIncome	Applicant's Monthly Income	Numerical (e.g., `5000`)
CoapplicantIncome	Co-applicant's Monthly Income	Numerical (e.g., `1500`)
LoanAmount	Requested Loan Amount ($ in thousands)	Numerical (e.g., `150`)
Loan_Amount_Term	Loan Tenure (in days / months)	Numerical (e.g., `360`)
Credit_History	Credit History Meets Guidelines	`1` (Good Credit), `0` (Poor Credit)
Property_Area	Property Location Type	`2` (Urban), `1` (Semiurban), `0` (Rural)
---
🚀 Installation & Setup
Prerequisites
Python 3.8+
pip (Python package installer)
Virtual Environment tool (`venv` or `conda` recommended)
Step 1: Clone or Navigate to Project Directory
```bash
cd "d:/Smart\\\_Lender\\\_Documentation/5. Project Development Phase/Smart\\\_Lender\\\_Code/Flask"
```
Step 2: Create & Activate Virtual Environment
On Windows:
```bash
  python -m venv venv
  .\\\\venv\\\\Scripts\\\\activate
  ```
On macOS/Linux:
```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
Step 3: Install Required Dependencies
```bash
pip install -r requirements.txt
```
Step 4: Run the Flask Web Application
```bash
python app.py
```
Open your web browser and navigate to: `http://127.0.0.1:5000/`
---
💻 Usage Guide
Launch the application using `python app.py`.
Access `http://127.0.0.1:5000/` in your browser.
Fill out the applicant loan form with relevant parameters (Income, Loan Amount, Credit History, etc.).
Click Submit / Predict.
View the real-time prediction result:
`Loan Approved ✅`: Applicant meets eligibility criteria.
`Loan Rejected ❌`: Applicant does not meet criteria based on risk factors.
---
📈 Model Training & Jupyter Notebook
The model training process is documented in `Smart Lender Using ML.ipynb` located in `Flask/Training/`.
To re-train or inspect the ML models:
Open Jupyter Notebook / JupyterLab:
```bash
   jupyter notebook "d:/Smart\\\_Lender\\\_Documentation/5. Project Development Phase/Smart\\\_Lender\\\_Code/Flask/Training/Smart Lender Using ML.ipynb"
   ```
Run data exploratory analysis, preprocessing steps, and model evaluations (XGBoost, Random Forest).
Export updated serialized model files (`xgb\\\_model.pkl` and `scale1.pkl`) to the `Flask/` directory.
---
📑 Project SDLC Phases
This repository stores documentation and deliverables corresponding to the 8 SDLC project stages:
Brainstorming & Ideation: Problem definition, empathy mapping, and solution prioritization.
Requirement Analysis: Data flow diagrams, tech stack selection, and customer journey mapping.
Project Design Phase: Architecture design and problem-solution fit documentation.
Project Planning Phase: Sprint planning, resource allocation, and timeline scheduling.
Project Development Phase: Full application code, ML notebook, Flask app, and dataset.
Project Testing: Model performance testing, validation metrics, and edge-case checks.
Project Documentation: Executable guide and complete technical documentation.
Project Demonstration: Demo script, video planning, scalability goals, and presentation outline.
---
🔮 Future Enhancements & Scalability
Real-Time Banking API Integration: Connect directly with credit bureau APIs (e.g., Experian, Equifax) for automated credit history verification.
Advanced Model Explainability: Integrate SHAP (SHapley Additive exPlanations) or LIME to provide applicants with explanations for rejection factors.
Cloud Deployment: Containerize with Docker and deploy on AWS Elastic Beanstalk / Azure App Service with CI/CD pipelines.
Enhanced UI/UX: Upgrade interface to modern web frameworks (React / Vue) with dynamic visualizations.
---
📜 License & Acknowledgments
Developed as part of the Smart Lender machine learning & software engineering project.
Dataset source: Public Loan Prediction Dataset.
Open-source components: Python, Flask, XGBoost, Scikit-Learn, Pandas, NumPy.
