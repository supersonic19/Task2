from django.urls import path
from main import views


urlpatterns = [
    path('' , views.info_view.as_view()),  
]