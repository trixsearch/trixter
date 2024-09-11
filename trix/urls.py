from django.urls import path
from . import views

urlpatterns = [
    path('', views.trix_list, name='trix_list'),
    path('create/', views.trix_create, name='trix_create'),
    path('<int:trix_id>/del/', views.trix_delete, name='trix_delete'),
    path('<int:trix_id>/edit/', views.trix_edit, name='trix_edit'),
    ]