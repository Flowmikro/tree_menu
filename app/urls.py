from django.urls import path

from . import views

urlpatterns = [
    path('<str:menu_name>/', views.menu_list, name='menu_list'),  # http://127.0.0.1:8000/menyu/
]
