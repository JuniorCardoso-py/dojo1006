from django.urls import path
from seller import views


urlpatterns = [
    path('', views.seller, name='seller'),
    path('seller_form', views.seller_create, name='seller_form'),
    ]
