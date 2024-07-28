import flask
from flask import render_template, jsonify, request  
from test import loan_status
app = flask.Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/predict', methods=['POST','GET'])
def predict_route():
    no_of_dependents = int(request.form.get("no_of_dependents"))
    education = request.form.get("education")
    if(education=="Graduate"):
        education=1
    else:
        education=0
    self_employed = request.form.get("self_employed")
    if(self_employed=="Yes"):
        self_employed=1
    else:
        self_employed=0
    income_annum = int(request.form.get("income_annum"))
    loan_amount = int(request.form.get("loan_amount"))
    loan_term = int(request.form.get("loan_term"))
    cibil_score = int(request.form.get("cibil_score"))
    residential_assets_value = int(request.form.get("residential_assets_value"))
    commercial_assets_value = int(request.form.get("commercial_assets_value"))
    luxury_assets_value = int(request.form.get("luxury_assets_value"))
    bank_asset_value = int(request.form.get("bank_asset_value"))
    result=loan_term
    status=loan_status(no_of_dependents,education,self_employed,income_annum,loan_amount,loan_term,
                        cibil_score,residential_assets_value,commercial_assets_value,luxury_assets_value,bank_asset_value)
    return render_template("main.html",loan_term=result,status=status)

if __name__ == '__main__':
    app.run(debug=True)
