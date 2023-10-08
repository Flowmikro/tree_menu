from django.urls import path

from . import views

urlpatterns = [
    path('<str:menu_name>/', views.menu_list, name='menu_list')
]
