from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.tests, name="tests"),
    path('reports/', views.listreports, name="reports"),
    path('reports/<pk>/', views.detailreport, name="detailreport"),
    path('reports/<pk1>/<pk2>/', views.userreports, name="userreport"),
    path('test/attend/<int:pk>/', views.attend, name="attend"),
    path('test/attend/<pk>/submit/', views.submit, name="submit"),
    path('test/view/<pk>/', views.report, name="report"),
    path('test/edit/<pk>/', views.editquestions, name="edit-questions"),
    path('test/delete/<pk>/', views.deletequestion, name="delete-question"),
    path('test/new/', views.setquestions, name="set-questions"),
    path('formula/', views.newformula, name="formula")
]
