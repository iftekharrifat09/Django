from django.urls import path
from . import views
urlpatterns = [
    path('', views.studentInfo, name='studentInfo'),
    path('seeStudnetInfo', views.seeStudentInfo, name='seeStudentInfo'),
    path('about/', views.about, name='about'),
    path('feedback/', views.feedback, name='feedback'),
    path('seeFeedback/', views.seefeedback, name='seeFeedback'),
]
