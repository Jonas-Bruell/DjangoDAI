from django.urls import path

from . import views

urlpatterns = [
    path('', views.bereken_worp, name='Bereken Worp')
]
