from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('performers/', views.performers_index, name='performers'),
    path('history/', views.history_index)
]
