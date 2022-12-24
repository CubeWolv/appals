from django.urls import path

from . import views

urlpatterns = [
    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
    path('aboutus/', views.about, name='about'),
]

