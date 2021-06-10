from django.urls import path
from seller import views


urlpatterns = [
    path('seller', views.seller, name='seller'),  
    ]