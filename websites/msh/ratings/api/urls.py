from django.urls import path
from .views import Rating_ListAPIView

urlpatterns = [
    path('api/', Rating_ListAPIView.as_view(), name='api')
]
