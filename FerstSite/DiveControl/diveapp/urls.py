from django.urls import path
from . import views
from diveapp.views import register  


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('index.html', views.index, name='index_html'),
]