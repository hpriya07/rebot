def loan_status(no_of_dependents,education,self_employed,income_annum,loan_amount,loan_term,
                        cibil_score,residential_assets_value,commercial_assets_value,luxury_assets_value,
                bank_asset_value):
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier

    data = pd.read_csv("dataset.csv")
    df = pd.DataFrame(data)
    df[' education'] = df[' education'].str.strip()
    df[' education'] = df[' education'].map({'Graduate': 1, 'Not Graduate': 0})
    df[' self_employed'] = df[' self_employed'].str.strip()
    df[' self_employed'] = df[' self_employed'].map({'Yes': 1, 'No': 0})
    df[' loan_status'] = df[' loan_status'].str.strip()
    df[' loan_status'] = df[' loan_status'].map({'Approved': 1, "Rejected": 0})

    x = df.drop(' loan_status', axis=1)
    y = df[' loan_status']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=None)
    dectree = DecisionTreeClassifier()
    dectree.fit(x_train, y_train)

    new_data = pd.DataFrame({
        'loan_id': [1001],
        ' no_of_dependents': [no_of_dependents],
        ' education': [education],
        ' self_employed': [self_employed],
        ' income_annum': [income_annum],
        ' loan_amount': [loan_amount],
        ' loan_term': [loan_term],
        ' cibil_score': [cibil_score],
        ' residential_assets_value': [residential_assets_value],
        ' commercial_assets_value': [commercial_assets_value],
        ' luxury_assets_value': [luxury_assets_value],
        ' bank_asset_value': [bank_asset_value]
    })
    prediction_new = dectree.predict(new_data[['loan_id',' no_of_dependents', ' education', ' self_employed', ' income_annum',
                                            ' loan_amount', ' loan_term', ' cibil_score', ' residential_assets_value',
                                            ' commercial_assets_value', ' luxury_assets_value', ' bank_asset_value']])
    print(prediction_new)
    if(prediction_new==[1]):
        return "your profile has a high chance of loan approval"
    else:
        return "profile has no chance for loan approval"

