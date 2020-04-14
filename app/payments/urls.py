from django.urls import path

from . import views

urlpatterns = [
    path('payment/charge/', views.ChargeAPI.as_view(), name='charge')
]