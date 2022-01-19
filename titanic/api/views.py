from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response


class TitanicPrediction(APIView):
    def post(self, request):
        data = request.data

        pclass = data['pclass']
        sex = data['sex']
        age = data['age']
        sibsp = data['sibsp']
        parch = data['parch']
        fare = data['fare']
        embarked = data['embarked']
        title = data['title']

        x = [[pclass,sex,age,sibsp,parch,fare,embarked,title]]
        randomforest = ApiConfig.randomforest
        prediction = randomforest.predict(x)
        if prediction == 0:
            prediction = 'Not Survived'
        elif prediction == 1:
            prediction = 'Survived'
        else:
            prediction = 'Error'
        response_dict = {"Prediction": prediction}
        return Response(response_dict, status=200)