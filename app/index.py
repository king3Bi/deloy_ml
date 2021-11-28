
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
            'code': -1,
            'msg': 'Nhập đầy đủ dữ liệu'
        })

    if result[0] == 0:
        return jsonify({
            'code': 0,
            'msg': 'Bạn có một sức khỏe rất tốt, hãy cố gắng duy trì'
        })
    elif result[0] == 1:
        return jsonify({
            'code': 1,
            'msg': 'Kết quả là có nguy cơ, '
                   'nhưng bạn đừng lo lắng, hãy bỏ những thói quen xấu ảnh hưởng tới sức khỏe, '
                   'luyện tập thể dục để có sức khỏe tốt'
        })
    else:
        return jsonify({
            'msg': ''
        })

if __name__ == '__main__':
    app.run(debug=True)
