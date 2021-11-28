
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

    df = pd.DataFrame(data)

    X = full_pipeline.fit_transform(df)

    try:
        result = randforest_clf.predict_proba(X)[:,1][0]
    except Exception as e:
        return jsonify({
            'code': 404,
            'msg': 'Nhập đầy đủ dữ liệu'
        })

    #print(result)
    data_result = {
        'code': 200,
        'percent': round(result*100, 2)
    }

    if result < 0.5:
        data_result['msg'] = 'Bạn có một sức khỏe rất tốt, hãy cố gắng duy trì'
    else:
        data_result['msg'] = 'Kết quả là có nguy cơ, ' \
                             'nhưng bạn đừng lo lắng, hãy bỏ những thói quen xấu ảnh hưởng tới sức khỏe, ' \
                             'luyện tập thể dục để có sức khỏe tốt'
    return data_result

if __name__ == '__main__':
    app.run(debug=True)
