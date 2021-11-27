
from app import app, randforest_clf, full_pipeline
from app.utils import getDataFromRequestPost
from flask import render_template, request, jsonify
import pandas as pd


@app.route('/', methods=['get'])
def index():
    return render_template('index.html')

@app.route('/api/predict', methods=['post'])
def predict():
    req = request.json
    # male	age	currentSmoker	cigsPerDay	BPMeds	prevalentStroke	prevalentHyp	diabetes	totChol	sysBP	diaBP	BMI	heartRate	glucose
    data = getDataFromRequestPost(req)
    print(data)

    df = pd.DataFrame(data)

    X = full_pipeline.fit_transform(df)

    try:
        result = randforest_clf.predict(X)
    except Exception as e:
        return jsonify({
            'msg': 'Nhập đầy đủ dữ liệu'
        })

    if result[0] == 0:
        return jsonify({
            'msg': 'Không có khả năng'
        })
    elif result[0] == 1:
        return jsonify({
            'msg': 'Có khả năng'
        })
    else:
        return jsonify({
            'msg': ''
        })

if __name__ == '__main__':
    app.run(debug=True)
