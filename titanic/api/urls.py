from django.urls import path
from .views import TitanicPrediction

urlpatterns = [
    path('titanic/', TitanicPrediction.as_view(), name = 'titanic_prediction'),
]