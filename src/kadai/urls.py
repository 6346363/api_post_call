from django.urls import path

from . import views
from .views import LogCreateView,LogListView

app_name = 'kadai'

urlpatterns = [
    path('',        LogListView.as_view(),  name='list'),
    path('create',  LogCreateView.as_view(),name='create'), 
]