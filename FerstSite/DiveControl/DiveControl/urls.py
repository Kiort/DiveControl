from django.contrib import admin
from django.urls import path, include
from diveapp import views as diveapp_view

 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diveapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('diveapp.urls')),
    
]