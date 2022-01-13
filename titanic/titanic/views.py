from django.shortcuts import render
from . import fake_model
from . import ml_predict

def home(request):
    return render(request, 'index.html')

def result(request):
    try:
        pclass = int(request.GET["pclass"])
        sex = int(request.GET["sex"])
        age = int(request.GET["age"])
        sibsp = int(request.GET["sibsp"])
        parch = int(request.GET["parch"])
        fare = int(request.GET["fare"])
        embarked = int(request.GET["embarked"])
        title = int(request.GET["title"])
        #prediction = fake_model.fake_predict(age)
        prediction = ml_predict.prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title)
    except:
        msg = 'All values are numeric. Please check your input and try again.'
        return render(request, 'index.html', {'error_msg': msg})
    return render(request, 'result.html', {'prediction': prediction})