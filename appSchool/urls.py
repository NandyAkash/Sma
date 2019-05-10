from django.urls import path
from django.urls import include, path
from .views import RegistrationAPIView

urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
]