from django.urls import path 
from . import views

urlpatterns = [
  path("<int:pk>/" , views.ProducDetailApiView.as_view())#localhost:8000/api
]
