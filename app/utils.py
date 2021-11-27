
def getDataFromRequestPost(request):
    return {
        'male': [int(request.get('male')) if request.get('male') else None],
        'age': [int(request.get('age')) if request.get('age') else None],
        'currentSmoker': [int(request.get('currentSmoker')) if request.get('currentSmoker') else None],
        'cigsPerDay': [int(request.get('cigsPerDay')) if request.get('cigsPerDay') else None],
        'BPMeds': [int(request.get('BPMeds')) if request.get('BPMeds') else None],
        'prevalentStroke': [int(request.get('prevalentStroke')) if request.get('prevalentStroke') else None],
        'prevalentHyp': [int(request.get('prevalentHyp')) if request.get('prevalentHyp') else None],
        'diabetes': [int(request.get('diabetes')) if request.get('diabetes') else None],
        'totChol': [int(request.get('totChol')) if request.get('totChol') else None],
        'sysBP': [float(request.get('sysBP')) if request.get('sysBP') else None],
        'diaBP': [float(request.get('diaBP')) if request.get('diaBP') else None],
        'BMI': [float(request.get('BMI')) if request.get('BMI') else None],
        'heartRate': [int(request.get('heartRate')) if request.get('heartRate') else None],
        'glucose': [int(request.get('glucose')) if request.get('glucose') else None]
    }