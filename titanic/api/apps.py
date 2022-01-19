from django.apps import AppConfig
import pickle


class ApiConfig(AppConfig):
    name = 'api'
    #Load ML model once and make it accessible 
    randomforest = pickle.load(open('titanic/titanic_model.sav', 'rb'))