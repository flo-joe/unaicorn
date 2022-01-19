from api.apps import ApiConfig

def prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title):
    #import pickle
    #randomforest = pickle.load(open('titanic/titanic_model.sav', 'rb'))
    x = [[pclass,sex,age,sibsp,parch,fare,embarked,title]]
    randomforest = ApiConfig.randomforest
    prediction = randomforest.predict(x)
    if prediction == 0:
        prediction = 'Not Survived'
    elif prediction == 1:
        prediction = 'Survived'
    else:
        prediction = 'Error'
    print(prediction)
    return prediction