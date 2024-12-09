from django.urls import path
from . import views
from diveapp.views import register  

urlpatterns = [
    path('', views.index, name='index'),

]