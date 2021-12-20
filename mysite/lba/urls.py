from django.urls import path
from . import views

urlpatterns = [
    path('', views.mode_choise),
    path('<int:id>/', views.mode_run),
]
