from django.urls import path # type: ignore
from .views import prediction_view

urlpatterns = [
    path('', prediction_view, name='prediction'),
]
