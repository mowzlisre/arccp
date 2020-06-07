from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('test/', views.tests, name="tests"),
    path('test/attend/<int:pk>/', views.attend, name="attend"),
    path('test/attend/<pk>/submit/', views.submit, name="submit"),
    path('test/view/<pk>/', views.report, name="report"),
    path('test/edit/<pk>/', views.editquestions, name="edit-questions"),
    path('test/new/', views.setquestions, name="set-questions"),
    path('formula/', views.newformula, name="formula")
]
