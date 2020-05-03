from django.urls import path

from . import views

urlpatterns = [
    path('', views.BankView.as_view()),
    path('checkout/', views.checkout, name='checkout'),
    path('last/', views.last, name='last'),

]