from django.urls import path
from . import views, c_views



urlpatterns=[
    path('', views.home, name='blog-home'),
    path('pgtrb/', views.pgtrb, name='pgtrb'),
    path('ugtrb/', views.ugtrb, name='ugtrb'),
    path('polytrb/', views.polytrb, name='polytrb'),
    path('enggtrb/', views.enggtrb, name='enggtrb'),
    path('tnset/', views.tnset, name='tnset'),
    path('sample/', views.sample, name='sample'),
    path('archives/', views.archives, name='archives'),
    path('about/', views.about, name='about'),
    #Console Views
    path('console/', c_views.console, name='console'),
    path('notfound/', c_views.error404, name='404'),
    #PostViews
    path('console/post/', c_views.newpost, name='newpost'),
    path('console/post/<int:pk>/', c_views.editpost, name='editpost'),
    path('console/post/<int:pk>/delete/', c_views.deletepost, name='deletepost'),
    #AnnouncementViews
    path('console/announcement/', c_views.newannouncement, name='newannouncement'),
    path('console/announcement/<int:pk>/', c_views.editannouncement, name='editannouncement'),
    path('console/announcement/<int:pk>/delete/', c_views.deleteannouncement, name='deleteannouncement'),
    #PageDetails & Website
    path('console/pages/<int:pk>/', c_views.pageedit, name='pageedit'),
    path('console/website/', c_views.websiteedit, name='websiteedit'),

]