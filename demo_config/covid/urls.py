from django.urls import path 
from covid import views

urlpatterns = [
    path('test', views.test),
    path('login', views.login.as_view(), name="login"),
    path('main', views.main.as_view(), name="main")
]