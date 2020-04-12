from django.urls import path

from . import views

urlpatterns = [
    path('payment/charge', views.HomePageView.charge, name='charge')
]