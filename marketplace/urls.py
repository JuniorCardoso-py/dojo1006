from django.urls import path
from marketplace import views

urlpatterns = [
    path('', views.index)
]
