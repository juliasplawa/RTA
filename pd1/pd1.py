from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():

    num1 = float(request.args.get('num1', 0))
    num2 = float(request.args.get('num2', 0))

    features = {'num1': num1, 'num2': num2}

    if num1 + num2 > 5.8:
        pred = 1
    else:
        pred = 0

    return jsonify(
        prediction=pred,
        features=features
    )
