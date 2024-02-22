from django.urls import path
from . import views

urlpatterns = [
    path('insert/', views.insert_data, name='insert_data'),
    path('search/', views.search_data, name='search_data'),
    path('', views.home, name='home'),
]
