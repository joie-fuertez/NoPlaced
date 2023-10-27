from django.urls import path
from NoPlace.views import

urlpatterns = [
    path('', views.SignUp.as_view(), name='index'),
]

