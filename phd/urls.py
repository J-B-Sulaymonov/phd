from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views

from .views import GrammarCorrectionView

urlpatterns = [
    path('', views.index,name="index"),
    path('tahrir', views.tahrir, name='tahrir'),
    path('', include('django.contrib.auth.urls')),
    path('api/correct-text/', GrammarCorrectionView.as_view(), name='correct-text'),
    # path('statistic', views.statistic, name='statistic'),

]
