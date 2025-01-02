from django.urls import path
from . import views
from diveapp.views import register  
from diveapp.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('index.html', views.index, name='index_html'),
    path('vlasnikclub/', VlasnikClubList.as_view(), name='vlasnikclib_list'),
    path('sviobjekti/', views.sviobjekti, name='lista_svih_objekta'),
    path('lokacije/', views.lokacije, name='lokacije'),
    path('pridruzi_se/<int:lokacija_id>/', views.pridruzi_se, name='pridruzi_se'),
    path('odjavi_se/<int:lokacija_id>/', views.odjavi_se, name='odjavi_se'),
    path('lokacije_list/', lokacija_list, name='lokacija_list'),
    path('logout/', LogoutView.as_view(), name='logout'),
]