from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index,name="index"),
    path('tahrir', views.tahrir, name='tahrir'),
    path('', include('django.contrib.auth.urls')),
    # path('statistic', views.statistic, name='statistic'),

]
