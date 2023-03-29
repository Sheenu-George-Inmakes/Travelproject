from . import views
from django.urls import path
urlpatterns=[
    path('',views.demo, name='demo'),
    path('contacts/', views.contacts, name='contacts'),
    path('dest/', views.destinations, name='dest'),
    path('elements/', views.elements, name='elements'),
    path('news/', views.news, name='news')

]