from django.urls import path
from . import views
from diveapp.views import register  
from diveapp.views import *


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('index.html', views.index, name='index_html'),
    path('vlasnikclub/', VlasnikClubList.as_view(), name='vlasnikclib_list'),
    path('sviobjekti/', views.sviobjekti, name='lista_svih_objekta'),
]