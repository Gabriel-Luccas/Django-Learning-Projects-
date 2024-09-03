# product urls

from django.urls import path
from . import views



urlpatterns = [
    # API read per pk localhost:8000/api/product
    path("<int:pk>/", views.ProducDetailApiView.as_view()),
    # API update per pk localhost:8000/api/product/update
    path("update/<int:pk>/", views.ProductUpdateApiView.as_view()),
    # API delete per pk localhost:8000/api/product/delete
    path("delete/<int:pk>/", views.ProductDeleteApiView.as_view()),
    # api list products # localhost:8000/api/product/list
    path("list/", views.ProducListApiView.as_view()),
    # api create product # localhost:8000/api/product/create
    path("create/", views.ProducCreateApiView.as_view()),
]
