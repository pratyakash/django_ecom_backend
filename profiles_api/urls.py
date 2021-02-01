from django.urls import path

from profiles_api import views

urlpatterns = [
    path('hello_view', views.HelloAPiView.as_view()),
]
