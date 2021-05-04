from django.urls import path 
from covid import views

urlpatterns = [
    path('test', views.test),
    path('login', views.login.as_view(), name="login"),
    path('', views.main.as_view(), name="main"),
    path('search_case', views.search_case.as_view(), name="search_case"),
    path('search_date', views.search_date.as_view(), name="search_date")
    # path('main', views.main.as_view(), name="")
]