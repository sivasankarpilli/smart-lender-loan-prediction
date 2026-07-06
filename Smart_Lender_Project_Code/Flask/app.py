from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open("xgb_model.pkl", "rb"))   # or rdf.pkl
scaler = pickle.load(open("scale1.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    features = [
        float(request.form['Gender']),
        float(request.form['Married']),
        float(request.form['Dependents']),
        float(request.form['Education']),
        float(request.form['Self_Employed']),
        float(request.form['ApplicantIncome']),
        float(request.form['CoapplicantIncome']),
        float(request.form['LoanAmount']),
        float(request.form['Loan_Amount_Term']),
        float(request.form['Credit_History']),
        float(request.form['Property_Area'])
    ]

    final = np.array(features).reshape(1,-1)

    final = scaler.transform(final)

    prediction = model.predict(final)

    if prediction[0] == 1:
        result = "Loan Approved ✅"
    else:
        result = "Loan Rejected ❌"

    return render_template("result.html",
                           prediction=result,
                           form_data=request.form)


if __name__ == "__main__":
    app.run(debug=True)
