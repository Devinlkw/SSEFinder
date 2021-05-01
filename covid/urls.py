from django.urls import path 
from . import views

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('fetchLoginData', views.loginAuthentication, name='fetch_login_data'),
    path('covid', views.MainView.as_view(), name='main'),

    path('test', views.test, name='test'),
    path('caseForm', views.CaseFormView, name='case-form'),
    path('eventForm', views.EventFormView, name='event-form'),
    path('addAttendance/<str:add_type><int:id_num>', views.AddAttendanceView, name='add-attendance')
]