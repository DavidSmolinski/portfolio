from django.urls import path
from . import views


urlpatterns = [
    path('submit/', views.submit_happiness, name='submit_happiness'),
    path('predict/', views.predict_happy_view, name='predict_happy_view'),
    path('home/', views.home_view, name='home_view'),
]
