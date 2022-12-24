from django.urls import path

from . import views

urlpatterns = [
    path('<id>/<name>/', views.index, name='index'),
]