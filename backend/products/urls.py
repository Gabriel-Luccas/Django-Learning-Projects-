# product urls

from django.urls import path
from . import views

urlpatterns = [
    # API read per pk localhost:8000/api/product
    path("<int:pk>/", views.ProducDetailApiView.as_view()),
    # api list products # localhost:8000/api/product/list
    path("list/", views.ProducListApiView.as_view()),
    # api create product # localhost:8000/api/product/create
    path("create/", views.ProducCreateApiView.as_view()),
]
