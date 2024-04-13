from django.urls import path
from first import views

urlpatterns = [path('signup', views.SignupView.as_view(), name='signup'),
               ]