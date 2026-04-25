from django.urls import path

from . import views

urlpatterns = [
    path('', views.bereken_worp, name='Bereken Worp'),
    path('item/<int:pk>/delete/', views.item_delete, name='item_delete')
]
